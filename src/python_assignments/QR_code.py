from pyzbar.pyzbar import decode
import qrcode 
from PIL import Image

myqr1=qrcode.make("www.linkedin.com/in/donia-batool-619691254")
myqr2=qrcode.make("https://drive.google.com/file/d/1ZJCmPJK-JQX6wrkzT4re7tk1LlOWbEfJ/view?usp=sharing")

myqr1.save("myqr1.png",scale=8)
myqr2.save("myqr2.png",scale=7)

a=decode(Image.open("myqr1.png"))
b=decode(Image.open("myqr2.png"))
print(a[0].data.decode("ascii"))
print(b[0].data.decode("ascii"))