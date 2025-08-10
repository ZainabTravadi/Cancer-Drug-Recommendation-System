from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes.analyze import router as analyze_router
import os

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
def api_status():
    return {"message": "Backend and frontend working."}

# API routes
app.include_router(analyze_router)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIST = os.path.join(BASE_DIR, "dist")
ASSETS_DIR = os.path.join(FRONTEND_DIST, "assets")

# Mount static files only if directory exists
if os.path.isdir(ASSETS_DIR):
    app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")

# Serve frontend
@app.get("/")
async def serve_index():
    index_path = os.path.join(FRONTEND_DIST, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "Frontend not built or index.html missing"}

@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    index_path = os.path.join(FRONTEND_DIST, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "Frontend not built or index.html missing"}

# Run with uvicorn when executed directly
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))  # default 10000
    uvicorn.run("main:app", host="0.0.0.0", port=port)
