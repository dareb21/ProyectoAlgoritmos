from PIL import Image
from pytesseract import *

# Aca colocarán la dirección de su máquina, solo que comentenla para no interferir con la máquina de los demás
# pytesseract.tesseract_cmd = r"C:\Users\Dareb\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open("img1.JPG")
text = pytesseract.image_to_string(img, lang='spa')
print(text)