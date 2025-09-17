# meeting-summarize ✨  
From speech to insight – Automatically generate meeting notes, analyze conversations, and prepare Indonesian ASR datasets.  

## 🚀 Project Description  
**meeting-summarize** is a toolkit designed to process long-form audio and turn it into meaningful insights.  
It can be used for:  
- 📝 Automatically generating meeting notes.  
- 🎙️ Analyzing interviews or podcasts.  
- 📊 Preparing ASR datasets for the Indonesian language.  

The project combines audio preprocessing, automatic speech recognition (ASR), and summarization powered by LLMs.  

---

## 🔄 Pipeline Overview  

### 1. **Preprocessing Audio**  
- Splits long recordings into smaller, manageable chunks.  
- Ensures better performance and accuracy for downstream ASR.  

### 2. **Speech-to-Text (ASR)**  
- Transcribes audio into text using [Whisper](https://github.com/openai/whisper).  
- Supports Indonesian language for accurate transcription.  

### 3. **Summarization**  
- Uses LLMs to summarize transcripts into concise meeting notes.  
- Extracts key points and actionable items.  

### 4. **Dataset Preparation**  
- Prepares paired **audio + transcript** datasets.  
- Useful for research or fine-tuning ASR models specifically for Indonesian.  

---

## 📌 Key Features  
- End-to-end pipeline: from raw audio to summarized text.  
- Flexible for different use cases (meetings, podcasts, research).  
- Supports Indonesian ASR dataset creation.  

---

## 🛠️ Tech Stack  
- **Python**  
- **Whisper** for ASR  
- **LLMs** for summarization  
- **Audio preprocessing** with standard libraries  

---

## 📂 Example Use Cases  
- Corporate meetings → Generate automatic minutes.  
- Podcasts/interviews → Extract insights without manual listening.  
- Research → Build custom Indonesian ASR datasets.  

---

## 📜 License  
MIT License. Feel free to use, modify, and contribute!  
