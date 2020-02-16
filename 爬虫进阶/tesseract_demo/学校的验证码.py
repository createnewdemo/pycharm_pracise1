import pytesseract
from PIL import Image
import time
from urllib import request
import base64


def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    url = 'https://www.jsdati.com/captcha/login?_=iz5uvdy4dk7'
    while True:
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        print(type(image))
        # text = pytesseract.image_to_string(image)
        # print(text)
        # time.sleep(3)


main()
