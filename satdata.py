import math
import rasterio
import numpy
import matplotlib.pyplot as plt

image_file = "image2.tif"
sat_data = rasterio.open(image_file)
print(sat_data.count)
b,g,r,n=sat_data.read()

# sequence of band indexes
print(sat_data.indexes)
fig = plt.imshow(n)
fig.set_cmap('inferno')
plt.colorbar
rgb=numpy.dstack((r,g,b))
nrb=numpy.dstack((n,r,b))
plt.imshow(rgb)