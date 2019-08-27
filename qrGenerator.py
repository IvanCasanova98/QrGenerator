import qrcode
import sys


def crearqr(nombre):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(nombre)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="white")
    img.save(nombre)


if '.txt' in sys.argv[1]:
    file = open(sys.argv[1], "r+")
    listName = file.readlines()
    print(listName)
