import numpy as np
from sklearn.metrics import confusion_matrix 
from scipy.spatial.distance import cdist 
from skimage.measure import label, regionprops, moments, moments_central, moments_normalized, moments_hu 
from skimage import io, exposure 
from skimage.filters import threshold_otsu
from skimage.morphology import binary_dilation
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle 
import pickle
import numpy as np
import os

'''
Reads a given image and binarizes it using a threshold
'''
def read_binarize(img_path, file_name):

    # read the given image
    img = io.imread(img_path)
    # use ostu method to find thresh val
    thresh = threshold_otsu(img)
    # binarize according to a threshold
    img_binary = (img < thresh).astype(np.double)
    # close gaps
    img_binary = binary_dilation(img_binary)
    # get all connected components
    img_label = label(img_binary, background=0)
    
    # finds all connected edges
    regions = regionprops(img_label)

    # stores the statistical information for the given image
    # NOTE: shape is number of regions by 7 for hu moments
    features = np.zeros((len(regions), 7))

    # for the image export of each character
    ax = plt.gca()
    io.imshow(img_binary)

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
        if width > 10 and height > 10:
            build_set(minr, minc, maxr, maxc, reg)
            ax.add_patch(Rectangle((minc, minr), maxc - minc, maxr - minr, fill = False, edgecolor = 'red', linewidth = 1))
    ax.set_title('Bounding Boxes')
    
    # Check whether the specified path exists or not
    if(not os.path.exists('./results/training_annotations')):
        os.makedirs('./results/training_annotations')
    
    # save our bounding boxes image
    plt.savefig("./results/training_annotations/{}.png".format(file_name))
    plt.close('all')

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

def get_preds(normalized, test_mat, num_neighbors):

    # keeps track of the locations of each letter array
    letter_locs = {}
    count = 0

    # store the distances between train and test and accuracy stuff
    total = 0
    corr = 0
    pred = []
    real = []

    acc = corr/total
    print('Training accuracy: ', acc)

    # create the label vector
    for k in normalized.keys():
        for i in range(count, count+len(normalized[k])):
            letter_locs[i] = k
        count += len(normalized[k])

    conc = np.concatenate([normalized[k] for k in normalized])

    D = cdist(conc, test_mat)
    D_index = np.argsort(D, axis=1)

    for i, d in enumerate(D_index):

        neighbors = []

        # find neighbors and take majority wins
        for n in range(num_neighbors):
            neighbors.append(letter_locs[d[1]])
        pred.append(max(set(neighbors), key=neighbors.count))
        real.append(letter_locs[i])

        if letter_locs[i] == letter_locs[d[1]]:
            corr += 1
        total += 1
	
    # for i in range(num_neighbors):
	# 	neighbors.append(distances[i][0])
    return pred, real, conc
