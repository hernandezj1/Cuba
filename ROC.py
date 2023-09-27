# Import the Image module from the Pillow Library, which will help us access the image.
from PIL import Image

# Import the pytesseract library, which will run the OCR process.
import pytesseract


# Open a specific image file, convert the text in the image to computer-readable text (OCR),
# and then print the results for us to see here.
print(pytesseract.image_to_string(Image.open(r"C:\Users\joseh\Cuba\textoimg\page0.jpg"), lang="spa"))