from PIL import Image, ImageFilter


im = Image.open('screenslide1.png')

blured_im = im.filter(ImageFilter.BLUR)
im_1 = im.convert("1")
im_L = im.convert("L")
im_LA = im.convert("LA")

blured_im.show()
im_1.show()
im_L.show()
im_LA.show()

blured_im.save("blured.png")
im_1.save("im_1.png")
im_L.save("im_L.png")
im_LA.save("im_LA.png")



