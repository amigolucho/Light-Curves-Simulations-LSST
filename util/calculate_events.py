# Calculate events
import os
from astropy.io import fits

base_dir = os.getenv('SNDATA_ROOT') + '/SIM'

objs = {}
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith("PHOT.FITS"):
         obj = file.split("_")[0]
         if obj not in objs: objs[obj] = 0

         file_path = os.path.join(root, file)
         light_curve = fits.open(file_path)[1].data
         objs[obj] += len(light_curve[light_curve["MJD"] == -777])

print(objs)
# falta escribirlos en algo
