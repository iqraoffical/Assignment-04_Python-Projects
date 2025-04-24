import qrcode
import cv2

# Create QR Code
def create_qr(data, filename="qr.png"):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR code saved as {filename}")

# Decode QR Code
def decode_qr(filename):
    detector = cv2.QRCodeDetector()
    img = cv2.imread(filename)
    data, _, _ = detector.detectAndDecode(img)
    return data

create_qr("https://example.com")
print("Decoded data:", decode_qr("qr.png"))







