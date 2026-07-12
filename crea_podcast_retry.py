import os
import re
import time
from gtts import gTTS

directory = r"C:\Users\Santo Penna\Downloads\ICT"
podcast_dir = os.path.join(directory, "Podcasts")

def clean_markdown(text):
    text = re.sub(r'#+\s*', '', text)
    text = re.sub(r'\*', '', text)
    text = re.sub(r'>\s*\[!.*?\]', 'Nota importante: ', text)
    text = re.sub(r'>\s*', '', text)
    text = re.sub(r'---', '', text)
    text = re.sub(r'\(file:///.*?\)', '', text)
    text = re.sub(r'\[(.*?)\]', r'\1', text)
    return text

# Solo i 3 file mancanti
missing_files = [
    "Svolgimenti_Temi_Profilo_C.md",
    "Temi_Prova_Scritta_Profilo_A.md",
    "Temi_Prova_Scritta_Profilo_C.md"
]

print(f"Rilancio generazione per {len(missing_files)} file mancanti...")

for filename in missing_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    
    clean_text = clean_markdown(text)
    
    # Salvataggio transcript
    transcript_filename = filename.replace('.md', '_transcript.txt')
    transcript_filepath = os.path.join(podcast_dir, transcript_filename)
    with open(transcript_filepath, 'w', encoding='utf-8') as transcript_file:
        transcript_file.write(clean_text)
    
    audio_filename = filename.replace('.md', '.mp3')
    audio_filepath = os.path.join(podcast_dir, audio_filename)
    
    print(f"Generazione in corso per: {filename} -> {audio_filename}")
    try:
        tts = gTTS(text=clean_text, lang='it', slow=False)
        tts.save(audio_filepath)
        print(f"Salvataggio completato: {audio_filename}")
    except Exception as e:
        print(f"Errore durante la generazione di {filename}: {e}")
    
    # Pausa di 10 secondi tra un file e l'altro per evitare il rate limiting
    time.sleep(10)

print("Generazione completata!")
