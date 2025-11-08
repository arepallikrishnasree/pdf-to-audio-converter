import PyPDF2
import pyttsx3
import argparse

def convert_pdf_to_audio(pdf_path):
    """PDF file nunchi text ni theesukoni, audio ga convert chestundhi."""
    
    # 1. PDF file open cheyyali
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            full_text = ""

            # 2. Prathi page nunchi text extract cheyyali
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text: # Empty text undakunda chusukovali
                    full_text += text + "\n"
            
            if not full_text.strip():
                print("Error: PDF file is empty or text extraction failed.")
                return

            # 3. Text-to-Speech Engine ni initialize cheyyali
            engine = pyttsx3.init()
            engine.setProperty('rate', 150) # Default speed

            # Output file name create cheyyali
            output_audio_file = pdf_path.replace('.pdf', '_audio.mp3')
            
            print(f"\n[INFO] PDF ni chadavadam start aindhi...")
            print(f"[INFO] Audio book ni save chesthunnam: {output_audio_file}")
            
            # 4. Extracted text ni audio file ga save cheyyali
            engine.save_to_file(full_text, output_audio_file)
            
            # 5. Process ni run chesi complete cheyyali
            engine.runAndWait()
            print("\n✅ Conversion successful! Mee audio book ready ga undhi.")

    except FileNotFoundError:
        print(f"\n❌ Error: The file '{pdf_path}' dorakaledhu. File name check cheyyandi.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    
    # 6. argparse setup - Command line nunchi arguments theesukodaniki
    parser = argparse.ArgumentParser(
        description='A Python script that converts a PDF file into an MP3 audio book.'
    )
    
    # Required argument: PDF file path
    parser.add_argument(
        'pdf_file', 
        type=str, 
        help='The path to the PDF file you want to convert.'
    )
    
    args = parser.parse_args()
    
    # Function ni call cheyyadam
    convert_pdf_to_audio(args.pdf_file)
