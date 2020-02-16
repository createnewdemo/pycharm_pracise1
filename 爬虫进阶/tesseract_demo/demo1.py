import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('c.png')

text = pytesseract.image_to_string(image, lang='chi_sim')

print(text)
