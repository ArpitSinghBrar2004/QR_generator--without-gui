import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5)

data=input("entter link you want qr of")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img .save("test.png")