'''
怎样训练自己的.traineddata请参见:
https://limour.top/309.html
'''
from Autolnstaller import keepInstalled
keepInstalled({'pytesseract', 'Pillow'})
from PIL import Image
import pytesseract, re
from io import BytesIO

fl = re.compile(r'[a-zA-Z-]+')
def clearStr(str):
    return ''.join(fl.findall(str))

config = '--psm 8'

def tesOCR(imgdata):
    img = Image.open(BytesIO(imgdata))
    return clearStr(pytesseract.image_to_string(img.convert("L"), lang='fdu', config=config))