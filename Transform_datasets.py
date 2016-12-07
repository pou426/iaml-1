# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import print_function
import os
from scipy.io.arff import loadarff
import pandas as pd

def arff2csv(filename, dataset_dir=None, force=False):
    if dataset_dir == None:
        dataset_dir = os.getcwd()
    if (os.path.isfile(filename + '.csv') and force == False):
        print('Dataset', filename, 'found, skipping...')
    else:
        print('Transforming dataset', filename, '...')
        try:
            dataset = loadarff(dataset_dir + '\\' + filename + '.arff')
            attributes = []
            for attribute in dataset[1]:
                attributes.append(attribute)
            df = pd.DataFrame(columns=attributes)
            for attribute in attributes: # Fill columns
                df[attribute] = dataset[0][attribute]
            df.to_csv(dataset_dir + '//' + filename + '.csv', index=False)
            print('Done.')
        except (IOError, ValueError, NotImplementedError):
            print('Transformation of dataset', filename, 'failed.')
            
def main(dataset_dir=None):
    """Transform all datasets."""
    if dataset_dir == None:
        dataset_dir = os.getcwd()
    dataset_files = os.listdir(dataset_dir)
    for dataset in dataset_files:
        if dataset.endswith('.arff'):
            dataset = os.path.splitext(dataset)[0]
            arff2csv(dataset, dataset_dir = dataset_dir, force=False)
    
if __name__ == "__main__":
    dataset_dir = "C:\\Users\\Agamemnon\\DTC\\Courses\\IAML - Introductory Applied Machine Learning\\Labs\\2016-2017\\datasets"
    main(dataset_dir=dataset_dir)