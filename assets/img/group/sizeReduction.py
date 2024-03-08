import os, sys
from PIL import Image

for infile in os.listdir():
    outfile = os.path.splitext(infile)[0] + "_reduced"
    if "_reduced" not in infile.split('.')[0] and (infile.endswith("jpg") or infile.endswith("png")):
        try:
            print(infile)
            im = Image.open(infile)
            rgbIm = im.convert('RGB')
            rgbIm.save(outfile + ".jpg", "JPEG", optimize=True)
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)