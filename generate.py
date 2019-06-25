import qrcode
from PIL import Image, ImageFont, ImageDraw
qr = qrcode.QRCode(
    version = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 14,
    border = 2,
)
data = "10001"
qr.add_data(data)
qr.make(fit=True)
qr_only = qr.make_image()
qr_only_file = data + ".bmp"
qr_only.save(qr_only_file)

img = Image.open("card_stage.png")  
  
img2 = Image.open(qr_only_file)  
img.paste(img2, (116, 20)) 
 
roboto = ImageFont.truetype("roboto.ttf", size=50)
width, height = img.size 

d = ImageDraw.Draw(img)
text = "QR Data: " + data
w, h = d.textsize(text,roboto)

location = (((width-w)/2,(height-h)/1.35)) 
text_color = (0,0,0)
d.text(location, text, font=roboto, fill=text_color)

roboto = ImageFont.truetype("roboto.ttf", size=30)
text = "Test"
w, h = d.textsize(text,roboto)
location = (((width-w)/2,(height-h)/1.14))
d.text(location, text, font=roboto, fill=text_color)

roboto = ImageFont.truetype("roboto_italic.ttf", size=40)
text = "Some Text"
w, h = d.textsize(text,roboto)
location = (((width-w)/2,(height-h)/1.09))
d.text(location, text, font=roboto, fill=text_color)

roboto = ImageFont.truetype("roboto.ttf", size=30)
text = "Another Text"
w, h = d.textsize(text,roboto)
location = (((width-w)/2,(height-h)/1.04))
d.text(location, text, font=roboto, fill=text_color)

img.save(data + ".jpg") 
