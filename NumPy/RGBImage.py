import numpy
from PIL import Image

# 100 x 100 array with each element as RGB
img=numpy.zeros((100,100,3),dtype=numpy.uint8)

img[:,:,0]=255
img[:,:,1]=numpy.linspace(0,255,100)
img[:,:,2]=50

image=Image.fromarray(img)
image.save("rgbimage.png")