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

    # stores the statistical information for the given image
    features = []

    # read the given image
    img = io.imread(img_path)
    # binarize according to a threshold
    img_binary = (img < thresh).astype(np.double)
    # get all connected components
    img_label = label(img_binary, background=0)

    # function to extract statistical info from each image
    def build_set(minr, minc, maxr, maxc):
        roi = img_binary[minr:maxr, minc:maxc]
        m = moments(roi)
        cr = m[0, 1] / m[0, 0]
        cc = m[1, 0] / m[0, 0]
        center = (cr, cc)
        mu = moments_central(roi, center)
        nu = moments_normalized(mu)
        hu = moments_hu(nu)
        features.append(hu)
    
    # finds all connected edges
    regions = regionprops(img_label)

    # build the set for each connected feature
    for props in regions:
        minr, minc, maxr, maxc = props.bbox
        height = maxr - minr
        width = maxc - minc
        if width > 5 and height > 5:
            build_set(minr, minc, maxr, maxc)

    return features

'''
Normalize the features by pushing the mean and variance to 0 and 1
'''
def normalize(features):

    # gather all the moments
    moments = []

    # loop through the keys and normalize the distributions of the different features
    for i in range(7):
        m = []
        for k in features.keys():
            image = features[k]
            for j,r in enumerate(image):
                m.append(image[j][i])
        moments.append(m)
    
    # find mean and std dev
    means = [np.mean(arr) for arr in moments]
    
    return means

