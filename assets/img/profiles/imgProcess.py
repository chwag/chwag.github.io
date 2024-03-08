import os, sys, glob
from PIL import Image, ImageOps

ratio = 1/1
inverseRatio = 1/ratio
size = (1024,1024)

infiles = glob.glob('*.png') + glob.glob('*.jpg')
for infile in infiles:
    if "_cropped" not in infile:
        try:
            print(infile)
            outfile = os.path.splitext(infile)[0] + "_cropped"
            im = Image.open(infile)
            fixedIm = ImageOps.exif_transpose(im) # This fixes the orientation, which may otherwise act funny due to metadata
            fullX,fullY = fixedIm.size
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
            croppedIm = fixedIm.crop(box)
            croppedIm.thumbnail(size)
            rgbIm = croppedIm.convert('RGB')
            rgbIm.save(outfile + ".jpg", "JPEG", optimize=True)
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)