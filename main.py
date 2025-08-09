from PyPDF2 import PdfReader
from gtts import gTTS
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re

def clean_text(text):
    # Replace multiple newlines and spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Add periods if missing at the end of paragraphs or lines (simple heuristic)
    # This is a naive approach, but helps gTTS pause better.
    text = re.sub(r'(?<![.!?])\s(?=[A-Z])', '. ', text)  # Add period before capital letters that start sentences
    
    return text.strip()

def pdf_to_audio(pdf_path, audio_path, lang='en'):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            full_text += page_text + "\n"

    cleaned_text = clean_text(full_text)
    tts = gTTS(text=cleaned_text, lang=lang)
    tts.save(audio_path)
    print(f"Audio saved as {audio_path}")

if __name__ == "__main__":
    Tk().withdraw()
    print("Select the PDF file to convert:")
    pdf_file = askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if not pdf_file:
        print("No file selected, exiting.")
        exit()

    audio_file = input("Enter desired output audio filename (e.g., output.mp3): ")
    pdf_to_audio(pdf_file, audio_file)
