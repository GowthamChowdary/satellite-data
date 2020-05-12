import math
import rasterio
import numpy
import matplotlib.pyplot as plt
#loading the image file

image_file = "#imgaddress"
sat_data = rasterio.open(image_file)

#number of bands in the image
print(sat_data.count)

nir=sat_data.read(1)
#normalizing the numpy array to facilitate plotting
def normalize(array):
    array_min,array_max=array.min(),array.max()
    return(array-array_min)/(array_max-array_min)

#plotting the image
from rasterio.plot import show
#show(sat_data)
nir_norm=normalize(nir)
plt.imshow(nir_norm)