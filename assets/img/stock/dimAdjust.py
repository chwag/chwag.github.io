## This code crops an image to the ratio 1/np.sqrt(2) or its inverse. As kwargs, provide the filename and the orientation of the final image.

import os, sys
import numpy as np
from PIL import Image

ratio = np.sqrt(2)
inverseRatio = 1/ratio
shortSide = 1024

infile = sys.argv[1]
outfile = os.path.splitext(infile)[0] + "_cropped"
if infile != outfile:
    try:
        im = Image.open(infile)
        fullX,fullY = im.size
        aspect = sys.argv[2]
        if aspect == "tall":
            size = (shortSide, shortSide * ratio)
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
        elif aspect == "wide":
            size = (shortSide * ratio, shortSide)
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
        croppedIm = im.crop(box)
        croppedIm.thumbnail(size)
        croppedIm.save(outfile + ".jpg", "JPEG", optimize=True)
    except IOError:
        print("cannot create thumbnail for '%s'" % infile)
