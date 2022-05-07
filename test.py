import PIL.Image


rgba_image = PIL.Image.open('B_1.png')
rgb_image = rgba_image.convert('RGB')
rgb_image.save('B_1_new.png')