# Connect file in src folder
from src.first_split_audio import split_audio
from src.second_load_audio_transcript import load_audio_transcript

AUDIO_PATH = "dataset/audio-1.mp3"
EXPORT_PATH = "dataset/split-audio-1"
CSV_PATH = "dataset/audio-1.csv"

# Split audio
chunks = split_audio(AUDIO_PATH, EXPORT_PATH)

# Load audio transcript
df = load_audio_transcript(CSV_PATH)

# Display results
print("Total chunks created:", len(chunks))
print("Audio Transcript DataFrame:", df.head())