from PIL import Image
from pyzbar.pyzbar import decode

def decode_qr_code(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Decode the QR code
    decoded_objects = decode(img)

    # Print the decoded text
    for obj in decoded_objects:
        print(f"Type: {obj.type}")
        print(f"Data: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    # Path to the image file containing the QR code
    image_path = "QR code.png"

    decode_qr_code(image_path)
