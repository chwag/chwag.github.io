import os, sys
from PIL import Image

ratio = 4/3
inverseRatio = 1/ratio
size = (512 * ratio, 512)

infile = sys.argv[1]
outfile = os.path.splitext(infile)[0] + "_cropped"
if infile != outfile:
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
    if sys.argv[2] == "jpg":
        croppedIm.save(outfile + ".jpg", "JPEG", optimize=True)
    elif sys.argv[2] == "png":
        croppedIm.save(outfile + ".png", "PNG", optimize=True)
    else:
        raise ValueError("Second kwarg not 'jpg' or 'png'")
