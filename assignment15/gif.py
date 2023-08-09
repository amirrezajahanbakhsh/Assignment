import os
import imageio

Gif = []

for image in sorted(os.listdir("assignment15/images")):
    image = imageio.v2.imread("assignment15/images/" + image)
    Gif.append(image)

imageio.mimsave("output.gif",Gif)