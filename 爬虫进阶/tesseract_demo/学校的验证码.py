import pytesseract
from PIL import Image
import time
from urllib import request
import base64


def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    url = 'http://m.langwx.net/hz/img/ding103.png'
    while True:
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        print(type(image))
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(3)


main()
