import qrcode

link = "https://68c90d338f5340784eb6e65d--amazing-pasca-63ef59.netlify.app/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("Aroma_qr.png")
