
#  Be name KHODA
#  author   :  Fateme Ordikhani  / FaOrdi
#  Date     :  23-12-25
#  Issue    :  payananme code
#  Date     :  1402-09-30
#  Version  :  0.01
#  Document :  README.md


import json
import numpy as np
import scipy
from scipy import io
from scipy.io import savemat
import csv


# input data
file_meta = "prbs15-2M-20dB.sigmf-meta"
file_data = "prbs15-2M-20dB.sigmf-data"

# Read data type   from json :
try:
    with open(file_meta, "r") as f:
        metadata = json.load(f)

    if 'global' in metadata and 'core:datatype' in metadata['global']:
        dtype = metadata['global']['core:datatype']
        print(dtype)
    else:
        raise ValueError("DataType (dtype) not specified in metadata.")

    #
    # np_dtype = None
    # if dtype == "cf32_le":
    #     np_dtype = np.complex64
    # elif dtype == "ci16_le":
    #     np_dtype = np.int16
    # else:
    #     raise ValueError(f"Unsupported SIGMF datatype '{dtype}' found in metadata.")

    # samples = np.memmap(file_data, mode='r', dtype=np_dtype)

except json.JSONDecodeError:
    raise ValueError("Error parsing JSON from metadata file.")
except FileNotFoundError:
    raise ValueError(f"Metadata file {file_meta} not found.")
except Exception as e:
    raise ValueError(f"An error occurred: {e}")

###########################################################
"""
# with open(file_meta, "r") as f:
#     md = json.loads(f.read())
# #
#
# dtype = md["global"].get("dtype", "ci16_le")
#
"""
# read file data sigmf   base on type meta:
try:
     if dtype == "cf32_le":
        samples = np.memmap(file_data, mode="r", dtype=np.complex64)
     elif dtype == "ci16_le":
        samples = np.memmap(file_data, mode="r", dtype=np.int16)
     else:
        print(f"Unknown dtype '{dtype}' in metadata. Using default dtype: np.complex64.")
        samples = np.memmap(file_data, mode="r", dtype=np.complex64)


#     print("Successfully read the file with dtype:", dtype)
except FileNotFoundError:
     print("Error: File not found.")
except Exception as e:
    print("Error:", e)



# choice sample of data
"""
# print(samples)
# samples_subset = samples[:50000]
# samples = samples_subset.astype(np.int16)
"""

# convert data  to  .csv

f = open('output01.csv', 'w')
writer = csv.writer(f)
writer.writerow(samples)
f.close()


print("==========================================")
# samples /= 32768
# samples = samples[::2] + 1j*samples[1::2]
# print(samples)





# convert to .mat

file_name = 'sample_file01.mat'

savemat(file_name, {'data': samples})
print(f"Data saved to {file_name}")



#===============================
# output_file = "output.iq"
# with open(output_file, 'wb') as f:
#
#     if dtype == "cf32_le":
#         samples.tofile(f)
#     elif dtype == "ci16_le":
#         samples.astype(np.int16).tofile(f)
#

# convert to .iq  format
output_file = "output01.iq"

import time
start_time = time.time()

with open(output_file, 'wb') as f:

    if dtype == "cf32_le":

        samples.tofile(f)
    elif dtype == "ci16_le":

        samples.astype(np.int16).tofile(f)
    else:

        raise ValueError(f"Unknown dtype '{dtype}' in metadata.")


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")


#Execution time: 86.40780210494995 seconds
