import numpy as np
from sklearn.metrics import confusion_matrix , accuracy_score
from scipy.spatial.distance import cdist 
from scipy import stats
from skimage.measure import label, regionprops, moments, moments_central, moments_normalized, moments_hu 
from skimage import io, exposure 
from skimage.filters import threshold_otsu
import skimage.morphology as skmp
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle 
import pickle
import os
from train import read_binarize, normalize, get_preds


def main(test_img):

    # first training
    features = {}
    directory_name = './H1-16images/'

    # go through all the images and get all the features
    for file_name in sorted(os.listdir(directory_name)):
        f = file_name.replace('.bmp', '')
        if f not in ('test1', 'test2'):
            features[f] = read_binarize(directory_name + file_name, f)
    
    # next normalize said features
    combined, flat, normalized, mean, std_dev = normalize(features)

    # dictionary to store training labels
    letter_locs = {}
    count = 0

    # create the label vector
    for k in normalized.keys():
        for i in range(count, count+len(normalized[k])):
            letter_locs[i] = k
        count += len(normalized[k])

    # K nearest neighbors on training data
    pred, real = get_preds(combined, combined, 3, letter_locs, letter_locs)
    acc = accuracy_score(real, pred)
    print('Training accuracy: ', acc)

    # Read testing data (image path, image name)
    test = read_binarize('./' + test_img, test_img)
    # NOTE: Recognition test image is saved in results with the bounding boxes
    test_norm_img  = (test - mean) / std_dev


