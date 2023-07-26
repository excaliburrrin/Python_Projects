import qrcode 

data = input("Enter a link for the QR code: ")

QRCodefile = input("Name your QR code and give type of the file: ")

QRimage = qrcode.make(data)

QRimage.save(QRCodefile)

print("Your QR code was successfully added to the folder.")