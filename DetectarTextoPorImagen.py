
#Bibliotecas necesarias: Pillow, pytesseract, pathlib, tkinter

from importlib.metadata import files
from tkinter.filedialog import askopenfilename
from PIL import Image
from pytesseract import *
from pathlib import Path
import tkinter as tk
import os
# Aca colocarán la dirección de su máquina, solo que comentenla para no interferir con la máquina de los demás
pytesseract.tesseract_cmd = r"C:\Users\Dareb\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def DetectarTextoPorImagen():
    file=askopenfilename()
    file_name=os.path.basename(file)
    print(file_name)
    text = pytesseract.image_to_string(Image.open(file_name))
    lbl_texto.config(text=text)
    #print(text)


root = tk.Tk()

root.geometry('800x500')
root.title("Detectar Texto de Imagen")
btn_convertir = tk.Button(root, text="Seleccione imagen", command=DetectarTextoPorImagen)
btn_convertir.place(x=50, y=150)

lbl_titulo = tk.Label(root, text="Su texto aparecera aqui: ")
lbl_titulo.place(x=50, y=200)
lbl_texto = tk.Label()
lbl_texto.place(x=50, y=300)

root.mainloop()

