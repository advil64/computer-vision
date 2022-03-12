import numpy as np
from sklearn.metrics import confusion_matrix 
from scipy.spatial.distance import cdist 
from skimage.measure import label, regionprops, moments, moments_central, moments_normalized, moments_hu 
from skimage import io, exposure 
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle 
import pickle
import numpy as np

'''
Reads a given image and binarizes it using a threshold
'''
def read_binarize(img_path, thresh):

    # read the given image
    img = io.imread(img_path)
    # binarize according to a threshold
    img_binary = (img < thresh).astype(np.double)
    # get all connected components
    img_label = label(img_binary, background=0)
    
    # finds all connected edges
    regions = regionprops(img_label)

    # stores the statistical information for the given image
    # NOTE: shape is number of regions by 7 for hu moments
    features = np.zeros((len(regions), 7))

    # function to extract statistical info from each image
    def build_set(minr, minc, maxr, maxc, region):
        roi = img_binary[minr:maxr, minc:maxc]
        m = moments(roi)
        cr = m[0, 1] / m[0, 0]
        cc = m[1, 0] / m[0, 0]
        center = (cr, cc)
        mu = moments_central(roi, center)
        nu = moments_normalized(mu)
        hu = moments_hu(nu)
        for p, h in enumerate(hu): features[region, p] = h

    # build the set for each connected feature
    for reg, props in enumerate(regions):
        minr, minc, maxr, maxc = props.bbox
        height = maxr - minr
        width = maxc - minc
        if width > 15 and height > 15:
            build_set(minr, minc, maxr, maxc, reg)

    # ignore all the rows with just zeros
    return features[~np.all(features == 0, axis=1)]

'''
Normalize the features by pushing the mean and variance to 0 and 1
'''
def normalize(features):

    # put together all of the matrices for different letters
    combined = np.concatenate([features[k] for k in features])
    flattned = combined.flatten()

    mean = np.mean(flattned)
    std_dev = np.std(flattned)

    # normalize the matrix
    norm_features = {}
    for k in features.keys(): 
        norm_features[k] = (features[k] - mean) / std_dev
    
    return combined, flattned, norm_features, mean, std_dev

