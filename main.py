import pyqrcode
import png
from pyqrcode import QRCode
link = "https://github.com/AyushSharma-007"
qr_code = pyqrcode.create(link)
qr_code.png("github.png", scale=5)
