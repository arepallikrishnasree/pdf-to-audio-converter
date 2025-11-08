import PyPDF2
import pyttsx3
import argparse
import os

def convert_pdf_to_audio(pdf_path, voice_type):
    """
    Extracts text from a PDF file and converts it into an audio file (MP3/WAV)
    with a fixed rate (150 WPM) and user-selected voice (Gender).
    """
    
    # 1. PDF file existence check
    if not os.path.exists(pdf_path):
        print(f"\n❌ Error: The file '{pdf_path}' was not found. Please check the file name.")
        return

    # 2. Open the PDF file
    try:
        # 'rb' stands for 'read binary'
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            full_text = ""

            # Extract text from each page
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text: 
                    # Add a newline for better text flow in the voice
                    full_text += text + "\n"
            
            if not full_text.strip():
                print("Error: PDF file is empty or text extraction failed. Please check the file content.")
                return

            # 3. Initialize the Text-to-Speech Engine
            engine = pyttsx3.init()
            
            # --- Voice Customization Logic ---
            
            # Fixed Rate set to 150 WPM (Your requested default speed)
            engine.setProperty('rate', 150) 
            
            # Set Voice Gender/Type
            voices = engine.getProperty('voices')
            
            target_voice = None
            if voice_type == 'male':
                target_voice = voices[0].id
            elif voice_type == 'female' and len(voices) > 1:
                target_voice = voices[1].id 
            
            if target_voice:
                engine.setProperty('voice', target_voice)
            # --- Customization Logic End ---
            
            # Create output file name
            output_audio_file = pdf_path.replace('.pdf', '_audio.mp3')
            
            print(f"\n[INFO] Starting PDF reading. Fixed Rate: 150 WPM, Voice: {voice_type.upper()}")
            print(f"[INFO] Saving audio book to: {output_audio_file}")
            
            # 4. Save the extracted text as an audio file
            engine.save_to_file(full_text, output_audio_file)
            
            # 5. Process and complete the operation
            engine.runAndWait()
            print("\n✅ Conversion successful! Your audio book is ready.")

    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    
    # argparse setup - To handle command-line arguments
    parser = argparse.ArgumentParser(
        description='A Python script that converts a PDF file into an MP3 audio book using a fixed rate (150 WPM).',
        epilog="Example: python converter.py 'my_document.pdf' --voice female"
    )
    
    # Required argument: PDF file path
    parser.add_argument(
        'pdf_file', 
        type=str, 
        help='The path to the PDF file you want to convert (Use quotes for files with spaces).'
    )
    
    # Optional argument: Voice Gender/Type
    parser.add_argument(
        '--voice', 
        type=str, 
        default='default', 
        choices=['male', 'female', 'default'],
        help='The preferred voice type (male, female, or default).'
    )
    
    args = parser.parse_args()
    
    # Call the function
    convert_pdf_to_audio(args.pdf_file, args.voice)