import os, sys, glob
from PIL import Image

infiles = glob.glob('*.png') + glob.glob('*.jpg') + glob.glob('*.jfif')
for infile in infiles:
    if "_reduced" not in infile:
        try:
            print(infile)
            outfile = os.path.splitext(infile)[0] + "_reduced"
            im = Image.open(infile)
            rgbIm = im.convert('RGB')
            rgbIm.save(outfile + ".jpg", "JPEG", optimize=True, quality=30)
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)