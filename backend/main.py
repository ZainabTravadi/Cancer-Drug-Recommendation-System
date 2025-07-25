from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes.analyze import router as analyze_router
import os

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get absolute paths safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "../neo-med-navigator"))

# Mount static folder
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Serve index.html at root
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# Optional API health check
@app.get("/status")
def api_status():
    return {"message": "✅ Cancer Drug Recommendation API is running."}

# Include /analyze routes
app.include_router(analyze_router)
