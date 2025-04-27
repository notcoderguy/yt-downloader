from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import subprocess
from typing import Optional, Dict
from pydantic import BaseModel
import uuid
import os
from datetime import datetime
import json
from pathlib import Path

app = FastAPI()

# Configure CORS - only allow from Laravel in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for download status
download_status: Dict[str, Dict] = {}
DOWNLOAD_DIR = Path("downloads")
STATUS_FILE = DOWNLOAD_DIR / "status.json"

class DownloadRequest(BaseModel):
    url: str
    format: Optional[str] = "mp4"
    quality: Optional[str] = "best"
    audio_only: Optional[bool] = False

class StatusResponse(BaseModel):
    status: str
    progress: Optional[float] = None
    output: Optional[Dict] = None
    error: Optional[str] = None
    created_at: str
    updated_at: str

def save_status():
    with open(STATUS_FILE, 'w') as f:
        json.dump(download_status, f)

def load_status():
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return {}

def process_download(task_id: str, url: str, format: str, quality: str, audio_only: bool):
    try:
        download_status[task_id] = {
            "status": "processing",
            "progress": 0,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        save_status()

        # Determine format based on audio_only flag
        if audio_only:
            format_spec = f"bestaudio[ext={format}]"
            output_template = f"downloads/%(title)s.%(ext)s"
        else:
            format_spec = f"bestvideo[ext={format}]+bestaudio[ext={format}]"
            output_template = f"downloads/%(title)s.%(ext)s"

        cmd = [
            "yt-dlp",
            "-f", format_spec,
            "--merge-output-format", format,
            "--newline",
            "--progress",
            "-o", output_template,
            url
        ]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in process.stdout:
            if "[download]" in line and "%" in line:
                progress = float(line.split("%")[0].split()[-1])
                download_status[task_id]["progress"] = progress
                download_status[task_id]["updated_at"] = datetime.now().isoformat()
                save_status()

        process.wait()

        if process.returncode == 0:
            download_status[task_id].update({
                "status": "completed",
                "progress": 100,
                "updated_at": datetime.now().isoformat()
            })
        else:
            download_status[task_id].update({
                "status": "failed",
                "error": process.stderr.read(),
                "updated_at": datetime.now().isoformat()
            })
        save_status()

    except Exception as e:
        download_status[task_id].update({
            "status": "failed",
            "error": str(e),
            "updated_at": datetime.now().isoformat()
        })
        save_status()

@app.post("/download")
async def download_video(request: DownloadRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    download_status[task_id] = {
        "status": "queued",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    save_status()

    background_tasks.add_task(
        process_download,
        task_id,
        request.url,
        request.format,
        request.quality,
        request.audio_only
    )

    return {"task_id": task_id}

@app.get("/status/{task_id}")
async def get_status(task_id: str):
    if task_id not in download_status:
        raise HTTPException(status_code=404, detail="Task not found")
    return download_status[task_id]

@app.get("/status")
async def list_status():
    return download_status

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Load existing status on startup
download_status = load_status()

# Ensure download directory exists
DOWNLOAD_DIR.mkdir(exist_ok=True)
