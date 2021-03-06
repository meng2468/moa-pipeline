import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def read_dataset(folder='./lish-moa/', include_non_score = False):
    '''
    return (train_features, train_targets, test_features, None/train_targets_nonscored)
    '''
    train_features = pd.read_csv(folder + 'train_features.csv')
    train_targets = pd.read_csv(folder + 'train_targets_scored.csv')

    test_features = pd.read_csv(folder + 'test_features.csv')

    train_targets_nonscored = None
    if include_non_score:
        train_targets_nonscored = pd.read_csv(folder + 'train_targets_nonscored.csv')

    return (train_features, train_targets, test_features, train_targets_nonscored)

def read_submission(folder):
    sample_submission = pd.read_csv(folder + 'sample_submission.csv')
    return sample_submission

def get_genes_cell_header(train_features):
    '''
    return (gense_heades, cells_header)
    '''

    GENES = [col for col in train_features.columns if col.startswith('g-')]
    CELLS = [col for col in train_features.columns if col.startswith('c-')]

    return (GENES, CELLS)

def generate_submission_csv(prediction, folder='./lish-moa/', outfile='submission.csv'):
    sample_submission = pd.read_csv(folder + 'sample_submission.csv')
    sample_submission.iloc[:,1:] = prediction

    # set ctl_vehicle to 0
    test_features = pd.read_csv(folder + 'test_features.csv')
    ignored_id = test_features[test_features['cp_type']=='ctl_vehicle'].sig_id

    sample_submission.loc[sample_submission.sig_id.isin(ignored_id),sample_submission.columns[1:]] = 0

    sample_submission.to_csv(outfile, index=False)
    print(f"Submission File saved: {outfile}")

    return sample_submission

def get_target_sample_count(train_targets):
    target_sample_count = train_targets.loc[:, train_targets.columns != 'sig_id'].sum().reset_index(name="counts").rename(columns={'index':'target'})
    return target_sample_count