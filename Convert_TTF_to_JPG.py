# import Image from wand.image module
import glob
from wand.image import Image
import os
# Read .png image using Image() function

final_root_dir= "/tmp//"

if not os.path.exists(final_root_dir):
    os.makedirs(final_root_dir)


for name in glob.glob('*.tif'):

    print(name)
    with Image(filename=name) as img:
        img.format = 'jpeg'
        name=name.split(".")
        print(name)
        img.save(filename=final_root_dir+ name[0] + '.jpg')