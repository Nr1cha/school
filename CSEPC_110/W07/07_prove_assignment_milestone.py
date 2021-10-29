import os 
# picture = os.path.join(os.getcwd(),'CSEPC_110/W07/beach.jpg')
from PIL import Image
print("the library is working correctly")


image_original = Image.open('CSEPC_110/W07/beach.jpg')

print(image_original.size)
print(image_original.format)

pixels_original = image_original.load()

print(pixels_original[200, 100])

#for 'range(x,x) it's the position on the image where the
#first 'x' in the sequence is starting on the left side of the image being 0
#the 2nd 'x' in the sequence is how far(in pixels) right to go

for y in range (0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_original[x, y]
        pixels_original[x, y] = (2, g, 255)

image_original.show()
# image_original.save('newThing.jpg')