from pydub import AudioSegment # library to process audio (cut, merge, convert, ect.)
import math # mathematics function (in this case for rounding up)
import os # access file in local

# function for chunk audio (60000ms or 1 minutes)
def split_audio(audio_path, export_path, chunk_length=60000):
    audio = AudioSegment.from_file(audio_path) # define audio
    num_chunks = math.ceil(len(audio) / chunk_length) # determine total chunk in audio
    os.makedirs(export_path, exist_ok=True) # create a folder if it doesn't exist

    chunks = [] # define chunks variable
    
    # looping for split audio into small chunk
    for i in range(num_chunks):
        start = i * chunk_length
        end = (i+1) * chunk_length
        chunk = audio[start:end]
        filename = os.path.join(export_path, f"clip{i+1}.mp3") 
        chunk.export(filename, format="mp3") 
        chunks.append(filename)
    return chunks