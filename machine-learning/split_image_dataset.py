import os
import glob
from shutil import copyfile

def split_dataset(PATH, valid_size=0.2):
    """
    Function that splits the full image dataset into training and validation
    sets.

    PATH is the root dir that contains a directory called 'data', with sub-directories for each 
    class/label that house the raw image files.

    """
    # set seed for reproducibility
    random.seed(42)

    # Create train and valid set dirs
    os.makedirs(f'{PATH}data_split/train')
    os.makedirs(f'{PATH}data_split/valid')

    for label in os.listdir(f'{PATH}data/'): # try on small set first
        if not label.startswith('.'):
            os.mkdir(f'{PATH}data_split/train/{label}')
            os.mkdir(f'{PATH}data_split/valid/{label}')

            # make list of all files in a labels directory
            t = glob.glob(f'{PATH}data/{label}/*.jpg')
            random.shuffle(t)
            # get validation set size (diff for each label)
            valid_len = int(valid_size * len(t))
            valid_files = t[:valid_len]
            train_files = t[valid_len:]

            # Move these files into the test/valid dirs inside the specific labels folder!
            for i in train_files:
                src = f'{i}'
                dst = f'{PATH}data_split/train/{label}/{i.rsplit("/", 1)[1]}'
                copyfile(src, dst)
            for i in valid_files:
                src = f'{i}'
                dst = f'{PATH}data_split/valid/{label}/{i.rsplit("/", 1)[1]}'
                copyfile(src, dst)