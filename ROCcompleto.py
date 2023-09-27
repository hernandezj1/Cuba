# 
import os
from PIL import Image
import pytesseract

path= r'C:\Users\joseh\Cuba\textoimg99on'


for image in os.listdir(path):

    inputPath = os.path.join(path, image) 
    img = Image.open(inputPath) 

        
     # Correr ROC
    ocrText = pytesseract.image_to_string(img, lang="spa")
            
    # Abrir file para compilar todo el texto
    with open("textocompleto.txt", "a", encoding="utf-8") as outFile:

        outFile.write(ocrText)
