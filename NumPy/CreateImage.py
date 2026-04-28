# pip install numpy
# pip install pillow

import numpy
from PIL import Image

# create a grayscale image
img=numpy.zeros((100,100),dtype=numpy.uint8)

for i in range(100):
    for j in range(100):
        img[i,j]=i+j

image=Image.fromarray(img)
image.save("gradient.png")

print("image saved...")