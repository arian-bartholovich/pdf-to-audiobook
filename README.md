# PDF to Audiobook

A **Python** command-line tool that converts PDF documents into spoken **audio (MP3)** using **text extraction** and **text-to-speech (TTS)**. Turn reports, articles, and study material into audio you can listen to on the go.

## Overview

Reading long documents is time-consuming and not always practical. This project automates the pipeline from a PDF file to an audio file: it extracts the text content, converts it to speech, and saves the result as an MP3.

## Key Features

<!-- TODO: Confirm each line against main.py, then edit or delete. -->

- **End-to-end automation:** PDF in, MP3 out, in a single script run
- **PDF text extraction:** reads text content from PDF documents [library: e.g., PyPDF2 / pypdf / pdfplumber]
- **Text-to-speech conversion:** generates natural-sounding audio [library: e.g., gTTS / pyttsx3]
- **Reproducible setup:** dependencies pinned in `requirements.txt`
- **Included sample:** `test-text.pdf` for quickly trying the tool

## Tech Stack

- **Language:** Python 3
- **Libraries:** [list from requirements.txt]
- **Output format:** MP3

## Project Structure

```
pdf-to-audiobook/
├── main.py            # Core script: extract text and generate audio
├── requirements.txt   # Python dependencies
├── test-text.pdf      # Sample input document
└── output.mp3         # Sample generated audio
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip
<!-- TODO: add an internet connection note if you use gTTS, or system speech engine note if pyttsx3 -->

### Installation

```bash
git clone https://github.com/arian-bartholovich/pdf-to-audiobook.git
cd pdf-to-audiobook
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

<!-- TODO: Explain how to choose the input PDF (edit a filename in main.py? command-line argument?) and where the MP3 is saved. -->

By default the script processes the included `test-text.pdf` and produces an MP3 audio file.

## Possible Enhancements

- Command-line arguments for input file, output file, and language
- Support for voice and speech-rate selection
- Chunked processing for very large PDFs
- OCR support for scanned documents
- Simple web or GUI front end

## Author

**Arian Bartholovich**
GitHub: [@arian-bartholovich](https://github.com/arian-bartholovich)
