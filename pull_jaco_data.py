from brainlit.utils.session import NeuroglancerSession
import pandas as pd
import numpy as np
from cloudvolume import CloudVolume, view
import math

# Loop through each of the 174 subvolumes and download the data locally
import boto3
from cloudvolume import Bbox

volumes_dir = "jaco_volumes/"
s3 = boto3.resource('s3')
bucket = s3.Bucket("open-neurodata")

mip = 2
dir = "s3://open-neurodata/brainlit/brain1"
dir_segments = "s3://open-neurodata/brainlit/brain1_segments"
neuroglancer = NeuroglancerSession(mip=mip, url=dir, url_segments=dir_segments)
res = neuroglancer.cv_segments.scales[neuroglancer.mip]["resolution"]

somas_prefix = "brainlit/brain1_somas/"
for vol_object in bucket.objects.filter(Prefix=somas_prefix):
    vol_key = vol_object.key
    vol_id  = os.path.basename(vol_object.key)
    if vol_id != "":
        vol_filepath = os.path.join(volumes_dir, f"{vol_id}.npy")
        bucket.download_file(vol_key, vol_filepath)
        coords = np.load(vol_filepath, allow_pickle=True)
        volume_coords = np.array(os.path.basename(vol_object.key).split("_")).astype(float)
        volume_vox_min = np.round(np.divide(volume_coords[:3], res)).astype(int)
        volume_vox_max = np.round(np.divide(volume_coords[3:], res)).astype(int)
        bbox = Bbox(volume_vox_min, volume_vox_max)
        volume = neuroglancer.pull_bounds_img(bbox)
