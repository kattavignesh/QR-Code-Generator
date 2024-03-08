#####################################################
__author__ = "VIGNESH"
__copyright__ = "Copyright (C) 2024 Author Vignesh"
__license__ = "Public"
__version__ = "1.0"
#####################################################

################
import pyqrcode
import png
################
print("Enter a link or name for generating a QR Code...")
link = input("") ### User Input Goes Here. ###
qr_code = pyqrcode.create(link)
qr_code.png("qrcode.png", scale=5) ### creates qr png in the folder with name as qrcode.png ###
