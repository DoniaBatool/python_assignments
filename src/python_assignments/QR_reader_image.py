from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("myqr1.png")  # apni QR code image ka naam likho
result = decode(img)

for qr in result:
    print("📦 Type:", qr.type)
    print("📄 Data:", qr.data.decode('utf-8'))
