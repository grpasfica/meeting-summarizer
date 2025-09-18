import pandas as pd
import whisper

# function to transcript audio using whisper
# for now not used whisper because it takes too long and not accurate for my audio
def transcribe_audio(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    return result["text"]

# Load the CSV file into a DataFrame (this data be obtained from manual transcription)
def load_audio_transcript(csv_path):
    df = pd.read_csv(csv_path)
    return df