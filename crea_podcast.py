import os
import re
from gtts import gTTS

directory = r"C:\Users\Santo Penna\Downloads\ICT"
podcast_dir = os.path.join(directory, "Podcasts")
os.makedirs(podcast_dir, exist_ok=True)

def clean_markdown(text):
    # Rimuove l'intestazione e i link alle fonti
    text = re.sub(r'#+\s*', '', text) # Rimuove i cancelletti
    text = re.sub(r'\*', '', text) # Rimuove gli asterischi
    text = re.sub(r'>\s*\[!.*?\]', 'Nota importante: ', text) # Sostituisce i tip/alert
    text = re.sub(r'>\s*', '', text) # Rimuove le virgolette blockquote
    text = re.sub(r'---', '', text) # Rimuove le linee di separazione
    text = re.sub(r'\(file:///.*?\)', '', text) # Rimuove i link testuali
    text = re.sub(r'\[(.*?)\]', r'\1', text) # Rimuove le parentesi quadre dai link
    return text

files = [f for f in os.listdir(directory) if f.endswith('.md')]
print(f"Trovati {len(files)} file Markdown. Inizio la generazione dei podcast...")

for filename in files:
    filepath = os.path.join(directory, filename)
    # Lettura in modalità sola lettura ('r')
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # La pulizia avviene solo in memoria
    clean_text = clean_markdown(text)
    
    # Salvataggio della copia pulita in un file di testo (transcript) per l'utente
    transcript_filename = filename.replace('.md', '_transcript.txt')
    transcript_filepath = os.path.join(podcast_dir, transcript_filename)
    with open(transcript_filepath, 'w', encoding='utf-8') as transcript_file:
        transcript_file.write(clean_text)
        
    audio_filename = filename.replace('.md', '.mp3')
    audio_filepath = os.path.join(podcast_dir, audio_filename)
    
    print(f"Generazione in corso per: {filename} -> {audio_filename}")
    try:
        # Usa la lingua italiana ('it')
        tts = gTTS(text=clean_text, lang='it', slow=False)
        tts.save(audio_filepath)
        print(f"Salvataggio completato: {audio_filename}")
    except Exception as e:
        print(f"Errore durante la generazione di {filename}: {e}")

print("Generazione dei podcast completata con successo!")
