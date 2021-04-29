#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:51:21 2021

@author: johnduva
"""

import sys
# sys.path.append("/Users/johnduva/Desktop/Git/NeuroData/brainlit") 

from brainlit.utils.session import NeuroglancerSession
# from brainlit.utils.swc import graph_to_paths
import napari
import pandas as pd
import numpy as np
import os
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import random
import cv2
from cloudvolume import CloudVolume, view
from tifffile import imsave
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as data
import torch.optim as optim
import sklearn.metrics

import pickle

# sys.path.append("/brainlit") 

dir = "s3://open-neurodata/brainlit/brain1"
vol = CloudVolume(dir, parallel=False, mip=2, progress=True, fill_missing=True)

stride = 4
final = coords = []

x1 = 0; x2 = vol.shape[0]
y1 = 0; y2 = vol.shape[1]
z1 = 0; z2 = vol.shape[2]

for x in range(x1, x2, 500,):
    x500 = x+500
    image = vol[x:x500, y1:y2, z1:z2] 

    '''  Create a list "final" with each element being a 12x12x12 subvolume within the designated region '''
    count = 0
    for xx in range(0, x500-x-(12-stride), stride ):
        for y in range(0, y2-y1-(12-stride), stride ):
            for z in range(0, z2-z1-(12-stride), stride ):
                final.append( image[xx:xx+12, y:y+12, z:z+12] )
                coords.append( [x+xx+6, y1+y+6, z1+z+6] ) # Keep track of the coordinates of each subvolume in "coords"
#                 print( [x+xx+6, y1+y+6, z1+z+6] ) # print the coords of each subvolume's center voxel
#                 print(image[xx:xx+12, y:y+12, z:z+12].shape) # print the shape of each subvolume
#                 print(' ')
                count +=1

    print("There are " + str(count) + " subvolumes.")

    outfile = open('final.pickle', 'wb')
    pickle.dump(final, outfile)
    outfile.close()

    outfile = open('coords.pickle', 'wb')
    pickle.dump(final, outfile)
    outfile.close()
