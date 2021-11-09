import os 
os.system("clear")
from PIL import Image

#FORMATTING
u = "\033[4m"
b = "\033[1m"
i = "\033[3m"
Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m"

#ARRAY STUFF
foreground_images = ["harvester","cactus","cat_small","cat","hiker","penguin","boat","spaceshuttle",]
background_images = ["earth","snowscape","desert","field","forest","sunset",]

#PRINT USER INPUT
print(f"{Green}{foreground_images}{Reset}\n")
user_foreground = input("pick a foreground image: ")
print(f"{Blue}{background_images}{Reset}\n")
user_background = input("pick a background image: ")

#IMAGES
BG_image = Image.open(f"{user_background}.jpg")
FG_image = Image.open(f"{user_foreground}.jpg")
image_combined = Image.new("RGB", FG_image.size)
FG_pixels = FG_image.load()
BG_pixels = BG_image.load()
pixels_new = image_combined.load()

#==========================
(width, height) = BG_image.size

#LOOP LOGIC
for y in range (0, height):
    for x in range(0, width):
        (red, green, blue) = FG_pixels[x, y]
        if green >= red + 40 and green >= blue + 40:
            (red, green, blue) = BG_pixels[x, y]
        pixels_new[x,y] = (red, green, blue)

# FG_image.show()
# BG_image.show()
image_combined.save("combined_image.jpg")
image_combined.show()