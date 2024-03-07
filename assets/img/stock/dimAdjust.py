import os, sys
import numpy as np
from PIL import Image

ratio = np.sqrt(2)
inverseRatio = 1/ratio

infile = sys.argv[1]
outfile = os.path.splitext(infile)[0] + "_cropped"
if infile != outfile:
    try:
        print(infile)
        im = Image.open(infile)
        fullX,fullY = im.size
        print(im.size)
        width = int(sys.argv[2])
        if width == 1:
            if fullY > ratio * fullX:
                newX = fullX
                spaceX = 0
                newY = fullX * ratio
                spaceY = (fullY - fullX * ratio) / 2
            elif fullY < ratio * fullX:
                newX = fullY * inverseRatio
                spaceX = (fullX - fullY * inverseRatio) / 2
                newY = fullY
                spaceY = 0
            else:
                newX = fullX
                spaceX = 0
                newY = fullY
                spaceY = 0
        elif width == 2:
            if fullX < ratio * fullY * 1.1:
                newX = fullX
                spaceX = 0
                newY = fullX * inverseRatio / 1.1
                spaceY = (fullY - fullX * inverseRatio / 1.1) / 2
            elif fullX > ratio * fullY * 1.1:
                newX = fullY * ratio * 1.1
                spaceX = (fullX - fullY * ratio * 1.1) / 2
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

# TODO add reduction of resolution