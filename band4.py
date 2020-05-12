import math
import rasterio
import numpy
import matplotlib.pyplot as plt
import time

# the satellite image file
image_file = "#imgaddress"


# function to make it easier to produce the spectral images.
def scenario(option, scheme):
    # loading the .tif file(satellite image)
    sat_data = rasterio.open(image_file)
    # reading the .tif file
    b, g, r, n = sat_data.read()

    if scheme == str('red'):
        fig = plt.imshow(r)
    elif scheme == str('blue'):
        fig = plt.imshow(b)
    elif scheme == str('green'):
        fig = plt.imshow(g)
    elif scheme == str('nir'):
        fig = plt.imshow(n)
    fig.set_cmap(option)


# calling the function by giving the required parameters
scenario('gist_heat', 'green')