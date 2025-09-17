import pandas as pd

# Load the CSV file into a DataFrame
def load_audio_transcript(csv_path):
    df = pd.read_csv(csv_path)
    return df