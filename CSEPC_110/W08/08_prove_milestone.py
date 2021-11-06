import os 
os.system("clear")
from PIL import Image

#IMAGES
BG_image = Image.open("earth.jpg")
FG_image = Image.open("spaceshuttle.jpg")
image_combined = Image.new("RGB", FG_image.size)
FG_pixels = FG_image.load()
BG_pixels = BG_image.load()
pixels_new = image_combined.load()

#==========================
(width, height) = BG_image.size

#LOOP LOGIC
for y in range (0, height):
    for x in range(0, width):
        (r, g, b) = FG_pixels[x, y]
        if g >= r + 40 and g >= b + 40:
            (r, g, b) = BG_pixels[x, y]
        pixels_new[x,y] = (r, g, b)

# FG_image.show()
# BG_image.show()
image_combined.save("combined_image.jpg")
image_combined.show()