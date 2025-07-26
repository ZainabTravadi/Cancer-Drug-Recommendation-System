from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes.analyze import router as analyze_router
import os

app = FastAPI()

# CORS (safe for now, restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Now using backend/dist (since dist is inside backend now)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIST = os.path.join(BASE_DIR, "dist")

app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="static")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIST, "index.html"))

# ✅ Optional: handle React Router routes (like /dashboard, /result)
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return FileResponse(os.path.join(FRONTEND_DIST, "index.html"))

# Health check
@app.get("/status")
def api_status():
    return {"message": "✅ Backend and frontend working."}

# API routes
app.include_router(analyze_router)
