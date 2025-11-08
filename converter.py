import PyPDF2 # PDF nunchi text chadavadaniki
import pyttsx3 # Text ni audio ga marusthundhi
import argparse
# 1. PDF file open cheyyali (Meeru convert cheyyalani anukuntunna file name ikkada petandi)
pdf_path = 'Kumar Garu invitation letter.pdf' # <--- Ee peru ni change cheyyandi!

# 'rb' ante 'read binary' mode lo open cheyyali
try:
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        full_text = ""

        # 2. Prathi page nunchi text extract cheyyali
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            full_text += text
            
        # 3. Text-to-Speech Engine ni initialize cheyyali
        engine = pyttsx3.init()
        
        # Voice speed set cheyyadaniki (Optional - normal ga 150-200 untundi)
        engine.setProperty('rate', 150) 
        
        # 4. Extracted text ni audio file ga save cheyyali
        output_audio_file = pdf_path.replace('.pdf', '_audio.mp3') # Ee peru tho save avuthundhi
        
        print(f"Converting PDF text to audio... Saving to: {output_audio_file}")
        engine.save_to_file(full_text, output_audio_file)
        
        # 5. Process ni run chesi complete cheyyali
        engine.runAndWait()
        print("Conversion successful! Audio book is ready.")

except FileNotFoundError:
    print(f"Error: The file '{pdf_path}' was not found. Please check the file name and path.")
except Exception as e:
    print(f"An error occurred: {e}") 
