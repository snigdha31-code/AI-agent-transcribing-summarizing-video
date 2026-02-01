# handles audio extraction and transcription

import subprocess # to run shell commands
import whisper #openai speach-to-text model
import os # to handle file operations

def extract_audio(video_path: str, audio_path:str="temp_audio.wav") -> str:
# Extracts audio from a video file and saves it as a WAV file.
    if os.path.exists(audio_path): # remove existing temp audio file
        os.remove(audio_path)
    command =[
        "ffmpeg",
        "-i", video_path, # input file
        "-q:a", "0", # audio quality to highest
        "-map","a", # selects audio track from video
        audio_path, # destination path for extracted audio
        "-y", # automatically overwrite existing files
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    # DEVNULL- excute commands in silent mode, check for errors, CHECKTRUE- raise exception if command fails
    return audio_path
    
def transcribe_audio(audio_path: str, model_size: str="base") -> str:
# passes the extracted audio to whisper model and returns the transcribed text
    model =whisper.load_model(model_size) # load the specified whisper model
    result = model.transcribe(audio_path) # transcribe the audio file
    transcript = result["text"] # extract the transcribed text from the result
    return transcript