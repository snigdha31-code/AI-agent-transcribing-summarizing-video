# AI AGENT TRANSCRIBING AND SUMMARIZING VIDEO

Convert any video into a concise summary using AI.

## Features
- Extracts audio from videos using FFmpeg
- Transcribes audio with OpenAI Whisper
- Summarizes text using Hugging Face Transformers (BART)
- Optional text chunking for long videos

## Tech Stack
- Python 3.11
- Whisper (OpenAI)
- Hugging Face Transformers
- FFmpeg

## Usage
```python
from main import video_to_summary

video_file = "sample_video.mp4"
summary = video_to_summary(video_file, use_chunking=True)
print(summary)
```
## Future Improvements
- Real-time transcription
- Multi-language support
- Domain-specific summarization
