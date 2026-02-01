# main.py
import whisper
from summarizer import summarize_text
from utils import chunked_summarize
from transcriber import extract_audio, transcribe_audio

def video_to_summary(
    video_file: str,
    model_size: str = "base",
    summarizer_model_name: str = "facebook/bart-large-cnn",
    use_chunking: bool = False
) -> str:
    
    print("Transcribing video...")
    transcript = extract_audio(video_file, "temp_audio.wav")
   
    print(f"Transcription completed. Length: {len(transcript)} characters")

    #  split into chunks if text is too long
    if use_chunking:
        # Simple chunking by 1000 characters
        chunks = [transcript[i:i+1000] for i in range(0, len(transcript), 1000)]
        summaries = [summarize_text(chunk, model_name=summarizer_model_name) for chunk in chunks]
        final_summary = " ".join(summaries)
    else:
        final_summary = summarize_text(transcript, model_name=summarizer_model_name)

    return final_summary

if __name__ == "__main__":
    video_file = "sample_video.mp4"  # Replace with your video path
    summary = video_to_summary(
        video_file,
        model_size="base",
        summarizer_model_name="facebook/bart-large-cnn",
        use_chunking=False
    )
    print("\n=== Final Summary ===\n")
    print(summary)
