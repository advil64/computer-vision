import numpy as np
from sklearn.metrics import confusion_matrix 
from scipy.spatial.distance import cdist 
from skimage.measure import label, regionprops, moments, moments_central, moments_normalized, moments_hu 
from skimage import io, exposure 
from skimage.filters import threshold_otsu
from skimage.morphology import binary_dilation, binary_closing
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
    thresh = 200#threshold_otsu(img)
    # binarize according to a threshold
    img_binary = (img < thresh).astype(np.double)
    # close gaps
    img_binary = binary_closing(img_binary)
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
        if width > 10 and height > 10:
            build_set(minr, minc, maxr, maxc, reg)

    # ignore all the rows with just zeros
    return features[~np.all(features == 0, axis=1)], regions

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

def get_preds(train, test, num_neighbors, train_labels, test_labels):

    # store the distances between train and test and accuracy stuff
    total = 0
    corr = 0
    pred = []
    real = []

    D = cdist(test, train)
    D_index = np.argsort(D, axis=1)

    for i, d in enumerate(D_index):

        neighbors = []

        # find neighbors and take majority wins
        for n in range(num_neighbors):
            neighbors.append(train_labels[d[n]])
        # pred.append(max(set(neighbors), key=neighbors.count))
        pred.append(train_labels[d[1]])
        real.append(test_labels[i])

        if test_labels[i] == train_labels[d[1]]:#max(set(neighbors), key=neighbors.count):
            corr += 1
        total += 1
	
    # for i in range(num_neighbors):
	# 	neighbors.append(distances[i][0])
    return pred, real

def label_img(img_name, labels, regions):
    
    # read the given image
    img = io.imread('./H1-16images/' + img_name + '.bmp')
    
    # for the image export of each character
    ax = plt.gca()
    io.imshow(img)

    # get the regions again and overlay labels
    for reg, props in enumerate(regions):
        minr, minc, maxr, maxc = props.bbox
        height = maxr - minr
        width = maxc - minc
        if width > 10 and height > 10:
            ax.add_patch(Rectangle((minc, minr), maxc - minc, maxr - minr, fill = False, edgecolor = 'red', linewidth = 1))
            try:
                ax.text(minc-20, minr-20, labels[reg], fontsize=11, verticalalignment='top')
            except:
                continue
    ax.set_title('{} Bounding Boxes'.format(img_name))
    
    # Check whether the specified path exists or not
    if(not os.path.exists('./results')):
        os.makedirs('./results')
    
    # save our bounding boxes image
    plt.savefig("./results/{}.png".format(img_name))
    plt.close('all')