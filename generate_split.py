''' Split data into training and testing datasets. '''
import numpy as np
import os

np.random.seed(2020) # to ensure you always get the same train/test split

data_path = '/Users/Johanna/Desktop/Computer Vision/hw01/RedLights2011_Medium'
gts_path = '../data/hw02_annotations/'
split_path = '../data/hw02_splits/'
preds_path = '../data/hw02_predictions/'
os.makedirs(preds_path, exist_ok=True) # create directory if needed

split_test = True # False splits filenames only, True splits images into separate files
train_frac = 0.85

# get sorted list of files:
file_names = sorted(os.listdir(data_path))
# remove any non-JPEG files:
file_names = [f for f in file_names if '.jpg' in f]
# split file names into train and test
file_names_train = []
file_names_test = []

'''
My code below. 
'''
file_names_train = np.random.choice(file_names, int(len(file_names)*0.85), replace=False)
file_names_test = [f for f in file_names if f not in file_names_train]

'''
My code above. 
'''

assert (len(file_names_train) + len(file_names_test)) == len(file_names)
assert len(np.intersect1d(file_names_train,file_names_test)) == 0

np.save(os.path.join(split_path,'file_names_train.npy'),file_names_train)
np.save(os.path.join(split_path,'file_names_test.npy'),file_names_test)

if split_test:
    with open(os.path.join(gts_path, 'annotations.json'),'r') as f:
        gts = json.load(f)
    
    # Use file_names_train and file_names_test to apply the split to the
    # annotations
    gts_train = {}
    gts_test = {}
    
    '''
    My code below. 
    '''
    for filename in file_names_train:
        gts_train[filename] = gts[filename]
    for filename in file_names_test:
        gts_test[filename] = gts[filename]

    '''
    My code above. 
    '''
    
    with open(os.path.join(gts_path, 'annotations_train.json'),'w') as f:
        json.dump(gts_train,f)

    with open(os.path.join(gts_path, 'annotations_test.json'),'w') as f:
        json.dump(gts_test,f)
    
    
