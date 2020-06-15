# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
from random import randint

# String which represents the QR code 
s = "www.google.com"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
#url.svg("myqr.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png(f'myqr-{randint(1,1000)}.png', scale = 6) 

