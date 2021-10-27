import os

import pandas as pd
import ast

from . import MOVIELENS_100K, MOVIELENS_1M, MOVIELENS_10M, EPINIONS
from ._descriptor_classes import DatasetDescriptor
from ._utils import make_dataset_path, make_ratings_file_path, download_and_extract_zip, download_and_extract_tar


def _transform_movielens_100k():
    raw_ratings = pd.read_csv(os.path.join(make_dataset_path(MOVIELENS_100K), 'ml-100k', 'u.data'),
                              sep='\t',
                              header=None,
                              names=['user_id', 'item_id', 'rating', 'timestamp'])

    raw_ratings.to_csv(make_ratings_file_path(MOVIELENS_100K),
                       sep=',',
                       index=None)


def _transform_movielens_1m():
    raw_ratings = pd.read_csv(os.path.join(make_dataset_path(MOVIELENS_1M), 'ml-1m', 'ratings.dat'),
                              sep='::',
                              header=None,
                              names=['user_id', 'item_id', 'rating', 'timestamp'])

    raw_ratings.to_csv(make_ratings_file_path(MOVIELENS_1M),
                       sep=',',
                       index=None)


def _transform_movielens_10m():
    raw_ratings = pd.read_csv(os.path.join(make_dataset_path(MOVIELENS_10M), 'ml-10M100K', 'ratings.dat'),
                              sep='::',
                              header=None,
                              names=['user_id', 'item_id', 'rating', 'timestamp'])

    raw_ratings.to_csv(make_ratings_file_path(MOVIELENS_10M),
                       sep=',',
                       index=None)


def _transform_epinions():
    raw_data = []
    with open(os.path.join(make_dataset_path(EPINIONS), 'epinions_data', 'epinions.json')) as f:
        for line in f:
            raw_data.append(ast.literal_eval(line))

    df = pd.DataFrame(raw_data)
    df['user_id'] = df['user'].astype('category').cat.rename_categories(range(1, df['user'].nunique() + 1))
    df['item_id'] = df['item'].astype('category').cat.rename_categories(range(1, df['item'].nunique() + 1))
    df = df[['user_id', 'item_id', 'stars', 'time']]
    df.rename(columns={'stars': 'rating', 'time': 'timestamp'}, inplace=True)

    df.to_csv(make_ratings_file_path(EPINIONS),
              sep=',',
              index=None)


def download_and_transform_dataset(dataset_descriptor: DatasetDescriptor, verbose=True):
    """Downloads a dataset by given descriptor.
    Next, transforms it into a CSV file that always contains columns 'user_id', 'item_id', 'rating'. Some additional columns may also
    be presented.
    This file can be found in os.path.join(dataset_descriptor.dir, RATINGS_FILE_NAME)
    """
    if dataset_descriptor.url.endswith('.zip'):
        download_and_extract_zip(dataset_descriptor.url, make_dataset_path(dataset_descriptor), verbose=verbose)
    elif dataset_descriptor.url.endswith('.tar.gz'):
        download_and_extract_tar(dataset_descriptor.url, make_dataset_path(dataset_descriptor), verbose=verbose)
    else:
        raise ValueError(f'Unknown archive format at url {dataset_descriptor.url}')

    if os.path.exists(make_ratings_file_path(dataset_descriptor)):
        if verbose:
            print(f'Dataset is already tranformed, skipped')
    else:
        if dataset_descriptor.id == MOVIELENS_100K.id:
            _transform_movielens_100k()
        elif dataset_descriptor.id == MOVIELENS_1M.id:
            _transform_movielens_1m()
        elif dataset_descriptor.id == MOVIELENS_10M.id:
            _transform_movielens_10m()
        elif dataset_descriptor.id == EPINIONS.id:
            _transform_epinions()

    if verbose:
        print(f'Dataset "{dataset_descriptor.name}" is ready for use')

