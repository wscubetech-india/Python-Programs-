import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/wscub/Desktop/Images2/images.png")

width , height = img.size

print (width,'x',height)