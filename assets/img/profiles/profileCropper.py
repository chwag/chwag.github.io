import os, sys
import numpy as np
from PIL import Image

ratio = 1/1
inverseRatio = 1/ratio

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_cropped"
    if infile != outfile:
        try:
            print(infile)
            im = Image.open(infile)
            fullX,fullY = im.size
            print(im.size)
            if fullX < ratio * fullY:
                newX = fullX
                spaceX = 0
                newY = fullX * inverseRatio
                spaceY = (fullY - fullX * inverseRatio) / 2
            elif fullX > ratio * fullY:
                newX = fullY * ratio
                spaceX = (fullX - fullY * ratio) / 2
                newY = fullY
                spaceY = 0
            else:
                newX = fullX
                spaceX = 0
                newY = fullY
                spaceY = 0

            box = (spaceX, spaceY, spaceX + newX , spaceY + newY)
            print(newX,newY)
            croppedIm = im.crop(box)
            croppedIm.save(outfile + ".png", "PNG")
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)