import os, sys, glob
from PIL import Image

ratio = 4/3
inverseRatio = 1/ratio
size = (512 * ratio, 512)

for infile in glob.glob('*.jpg'):
    if "_cropped" not in infile:
        try:
            outfile = os.path.splitext(infile)[0] + "_cropped"
            im = Image.open(infile)
            fullX,fullY = im.size
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
            croppedIm = im.crop(box)
            croppedIm.thumbnail(size)
            croppedIm.save(outfile + ".jpg", "JPEG", optimize=True)
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)