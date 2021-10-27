from PIL import Image
print("the library is working correctly")
image_original = Image.open("beach.jpg")
print(image_original.size)
print(image_original.format)
# image_original.show()
#load pixels
pixels_original = image_original.load()


print(pixels_original[222, 100])
pixels_original[222,100] = (255, 0, 255)
pixels_original[223,100] = (255, 0, 255)
pixels_original[224,100] = (255, 0, 255)
pixels_original[225,100] = (255, 0, 255)
pixels_original[226,100] = (255, 0, 255)
image_original.show()



