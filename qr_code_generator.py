import qrcode

data=input("Enter the text or URL you want to generate QR code for: ").strip()
filename=input("Enter the name of the file : ").strip()
qr=qrcode.QRCode(box_size=10,border=5)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(filename+".png")
print(f"QR code generated successfully as {filename}.png")