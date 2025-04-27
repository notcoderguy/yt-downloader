# YouTube Downloader Project

⚠️ **Important Notice**: This project is for **educational purposes only**. Downloading YouTube videos violates YouTube's Terms of Service. The author provides no guarantees or support for this software and is not responsible for any misuse.

## Project Description

A full-stack application for educational demonstration of downloading, managing and processing YouTube videos.

## Project Structure

```bash
yt-downloader/
├── web/                      # React frontend with shadcn UI
├── api/                      # FastAPI backend
├── docker-compose.yml        # Docker compose configuration
└── Dockerfile                # Docker configuration
```

## Technologies

### Frontend

- React with TypeScript
- React Router for navigation
- shadcn/ui for UI components
- Axios for API calls
- Bun (runtime and package manager)

### Backend

- Python FastAPI
- SQLAlchemy (ORM)
- Alembic (database migrations)
- Celery (for async tasks like video downloads)
- yt-dlp (for YouTube downloads)
- FFmpeg (for video processing)
- uv (Python package installer)

## Features

1. **User Authentication**
   - Registration (first-time users)
   - Login
   - Session management

2. **Video Management**
   - Download YouTube videos
   - Library of downloaded videos
   - Video metadata storage
   - Search and filtering

3. **Video Processing**
   - Trim videos
   - Extract audio
   - Convert formats
   - Quality selection

4. **System Features**
   - Background task processing
   - Progress tracking
   - Error handling

## Development Tasks

### Frontend Setup

1. Initialize React project with TypeScript
2. Add shadcn/ui components
3. Set up React Router
4. Create authentication pages (login/register)
5. Build video library interface
6. Create video processing UI
7. Implement API service layer

### Backend Setup

1. Initialize FastAPI project
2. Configure database connection
3. Set up authentication system (JWT)
4. Implement YouTube download endpoint
5. Create video processing endpoints
6. Set up Celery for async tasks
7. Implement file storage system

### Database

1. Design user schema
2. Design video metadata schema
3. Set up migrations
4. Implement CRUD operations

### Docker Setup

1. Create Dockerfile for frontend
2. Create Dockerfile for backend
3. Configure docker-compose.yml
4. Set up networking between services
5. Configure volumes for persistent storage

## Getting Started

### Prerequisites

- Node.js (for frontend)
- Python 3.9+ (for backend)
- Docker (for containerization)
- FFmpeg (for video processing)

### Installation

1. Clone the repository
2. Set up frontend:

   ```bash
   cd frontend
   bun install
   bun run dev
   ```

3. Set up backend:

   ```bash
   cd backend
   uv sync
   uvicorn main:app --reload
   ```

4. Run with Docker:

   ```bash
   docker-compose up --build
   ```

## Contribution Guidelines

- Follow conventional commits
- Write unit tests for new features
- Document API endpoints
- Maintain consistent code style

## License

This project is released under [The Unlicense](https://unlicense.org/), meaning it is completely free and unencumbered software released into the public domain.