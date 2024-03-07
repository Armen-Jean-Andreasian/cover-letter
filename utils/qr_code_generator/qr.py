import qrcode
from utils.export_binary import export_file


def qr_builder(message: str) -> None:
    data = message
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    export_file(img.save, "OUTPUT_FOLDER/qrcode.png")
