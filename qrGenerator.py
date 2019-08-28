import qrcode
import sys
from PIL import Image

def qrcodepreset():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    return qr


def crearqr(nombre):
    qr = qrcodepreset()
    qr.add_data(nombre)
    qr.make(fit=True)
    imgqr = qr.make_image(fill_color="black", back_color="white")
    imgqr.save(nombre + '.png')


def crearentrarda(nombre, imagen):
    qr = qrcodepreset()
    qr.add_data(nombre)
    qr.make(fit=True)
    imgqr = qr.make_image(fill_color="black", back_color="white")
    entrada = Image.open(imagen)
    entrada.paste(imgqr, (100, 100))
    entrada.save(nombre + ".jpg")


def error():
    print("Sintax error! \npython qrGenerator.py [nombre] \npython qrGenerator.py [archivo.txt] \n")
    sys.exit(0)


if len(sys.argv) >= 1 & len(sys.argv) <= 2:
    if '.txt' in sys.argv[1]:
        file = open(sys.argv[1], "r+")
        listName = file.readlines()
        for name in listName:
            if '.jpg' in sys.argv[2]:
                crearentrarda(name.replace('\n', ""), sys.argv[2])
            else:
                crearqr(name.replace('\n', ""))
    elif sys.argv[1].strip():
        crearqr(sys.argv[1])
else:
    error()
