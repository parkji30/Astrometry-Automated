import numpy as np
import os
import astropy
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
from scipy.stats import binned_statistic


def ImSave(image, title='', im_name='', directory=''):
    """
    Save the image as pngs.
    """
    image_name = im_name.split(".")
    image_name = image_name[0]
    im = Image.fromarray(image)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.save(directory + image_name + ".png")
    
def gaussian_filter(image, flat_field, im_nm='', directory=''):
    """
    Gaussian filter the images
    """
    
    # Original image mean subtraction
    image_og = image - np.mean(image)

    # Image after Flat Field Reduction
    image_al = image / flat_field
    image_al -= np.mean(image_al)
    
    # Apply Gaussian Filtering To the Image. Change vmin, vmax for scaling.
    lp_filter = ndimage.gaussian_filter(image_al, sigma=5)
    gauss_filter = ndimage.gaussian_filter(image_al - lp_filter, sigma=3)

    ImSave(image=gauss_filter, title='(Gaussian Filtered) flat field reduced', im_name = im_nm, directory=directory)