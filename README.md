# YouTube Downloader - Laravel Application

⚠️ **Important Notice**: This project is for **educational purposes only**. Downloading YouTube videos violates YouTube's Terms of Service. The author provides no guarantees or support for this software and is not responsible for any misuse.

A Laravel application for educational demonstration of downloading, managing and processing YouTube videos using yt-dlp and ffmpeg.

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
   - Extract subtitles and audio
   - Convert formats (mp4, webm, etc.)
   - Change resolution (1080p, 720p, etc.)
   - Generate thumbnails
   - Quality selection

4. **System Features**
   - Background task processing
   - Progress tracking
   - Error handling

## Requirements

- PHP 8.1+
- Composer
- Node.js (for frontend assets)
- MySQL/PostgreSQL/SQLite
- ffmpeg (for video processing)
- yt-dlp (for video downloads)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-repo/video-library-manager.git
cd video-library-manager
```

2. Install PHP dependencies:
```bash
composer install
```

3. Install JavaScript dependencies:
```bash
npm install
```

4. Create and configure `.env` file:
```bash
cp .env.example .env
```

5. Generate application key:
```bash
php artisan key:generate
```

6. Run database migrations:
```bash
php artisan migrate
```

7. Install ffmpeg and yt-dlp:
```bash
# On Ubuntu/Debian
sudo apt-get install ffmpeg
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

## Configuration

Configure these environment variables in `.env`:

```ini
# Video processing settings
FFMPEG_PATH=/usr/bin/ffmpeg
YTDLP_PATH=/usr/local/bin/yt-dlp
STORAGE_PATH=storage/app/videos
MAX_DOWNLOAD_SIZE=500M
```

## Usage

### Downloading Videos

Use the web interface or API to download videos by providing URLs.

### Processing Videos

Available processing options:
- Extract audio (`mp3`, `wav`, etc.)
- Extract subtitles
- Convert formats (`mp4`, `webm`, etc.)
- Change resolution (1080p, 720p, etc.)
- Generate thumbnails

### API Endpoints

- `POST /api/download` - Start a download
- `GET /api/videos` - List downloaded videos
- `POST /api/videos/{id}/process` - Process a video

## Queue Processing

For better performance, configure queue workers:

```bash
php artisan queue:work
```

## Development

1. Run the development server:
```bash
php artisan serve
npm run dev
```

2. Run tests:
```bash
php artisan test
```

## Contribution Guidelines

- Follow conventional commits
- Write unit tests for new features
- Document API endpoints
- Maintain consistent code style

## License

This project is released under [The Unlicense](https://unlicense.org/), meaning it is completely free and unencumbered software released into the public domain.
