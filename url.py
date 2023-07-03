import qrcode

url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"   # URL to encode
filename = "qr_code.png"  # The filename to save the QR code image

# Generate the QR code
img = qrcode.make(url)

# Save the QR code image
img.save(filename)
