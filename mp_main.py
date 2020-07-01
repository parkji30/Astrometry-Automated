"""
An auto script to record solutions using astrometry (solve-field)

Currently this only works for one folder of images.
"""

## PATHS AND IMPORTS
import os
os.chdir("/home/james/Desktop/astrometry_solutions_script")
from multiprocessing import Pool
import numpy as np
import astropy
import helper_functions

# Folder containing the program
HOME = "/home/james/Desktop/astrometry_solutions_script"

# Folder that contains raw images.
RAW_IMAGES ="/home/james/Desktop/astrometry_solutions_script/raw_images"

# Folder that will or already contains filtered images.
CLEANED_IMAGES_PATH = '/home/james/Desktop/astrometry_solutions_script/clean_images/'

# Folder that will save junk from astrometry
SOLVED_IMAGES_PATH =  '/home/james/Desktop/astrometry_solutions_script/solve_field_images/'


## IMAGE CLEANING
os.chdir(HOME)
xsc1_flat_field = np.load("xsc1_flat_field.npy")

os.chdir(RAW_IMAGES)
for fits_file in os.listdir(RAW_IMAGES):
    hdul = astropy.io.fits.open(fits_file)
    image_array = hdul[0].data
    helper_functions.gaussian_filter(image_array, xsc1_flat_field, im_nm=fits_file, directory=CLEANED_IMAGES_PATH)


## SOLVE FIELD SCRIPT
# Change this variable to add any extra syntax from astometry
# More info can be found at http://astrometry.net/doc/readme.html

os.chdir(CLEANED_IMAGES_PATH)

# List images and remove solutions.txt from the list.
images = os.listdir(CLEANED_IMAGES_PATH)
images.remove("solutions.txt")
images.sort()

def solve_field(image):

    # print(image)
    ASTROMETRY_TERMINAL_COMMAND = 'solve-field --scale-units arcsecperpix --scale-low 6.000 --scale-high 7.000 ' + image +\
                    ' --overwrite --dir /home/james/Desktop/astrometry_solutions_script/solve_field_images --cpulimit 100'

    # print(ASTROMETRY_TERMINAL_COMMAND)

    os.system(ASTROMETRY_TERMINAL_COMMAND)
    rtn = os.popen(ASTROMETRY_TERMINAL_COMMAND).read()
    
    rtn_list = rtn.split("\n")
    results_list = []
    
    for item in rtn_list:
        if "Field 1 did not solve" not in item:
            results_list.append(item)
       
    solution_values = []
            
    for item in results_list:
        if 'Field' in item:
            if "RA" in item or "Dec" in item or "size" in item or "rotation" in item:
                solution_values.append(item)
            
    values = []  
                
    for it in solution_values:
        if '=' in it:
            # print((it.split('=')))
            values.append(it.split('=')[-1])
        elif ':' in it:
            # print(it.split(":"))
            values.append(it.split(':')[-1])
        
    line = ''
    for value in values:
        line = line + value + '   '
    
    line = image + '                    ' + line
    
    f = open("solutions.txt", 'a')
    f.write(line)
    f.write('\n')
    f.close()
    os.system("clear")

if __name__ == '__main__':
    with Pool(4) as p:
        print(p.map(solve_field, images))
