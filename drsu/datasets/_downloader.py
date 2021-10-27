import datetime
import gzip
import json
import os

import pandas as pd
import ast

from . import MOVIELENS_100K, MOVIELENS_1M, MOVIELENS_10M, EPINIONS, LIBRARY_THING, GOODREADS_REVIEW_SPOILERS
from ._descriptor_classes import DatasetDescriptor
from ._utils import make_dataset_path, make_ratings_file_path, download_and_extract_zip, download_and_extract_tar, \
    download_and_extract_from_google_drive


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


def _transform_library_thing():
    raw_data = []
    with open(os.path.join(make_dataset_path(LIBRARY_THING), 'lthing_data', 'reviews.json')) as f:
        for line in f:
            raw_data.append(ast.literal_eval(line))

    df = pd.DataFrame(raw_data)
    df['user_id'] = df['user'].astype('category').cat.rename_categories(range(1, df['user'].nunique() + 1))
    df['item_id'] = df['work'].astype('category').cat.rename_categories(range(1, df['work'].nunique() + 1))
    df = df[['user_id', 'item_id', 'stars', 'unixtime']]
    df.dropna(inplace=True)
    df.rename(columns={'stars': 'rating', 'unixtime': 'timestamp'}, inplace=True)

    df.to_csv(make_ratings_file_path(LIBRARY_THING),
              sep=',',
              index=None)


def _transform_goodreads_reviews_spoliers():
    data = []
    with gzip.open(
            os.path.join(make_dataset_path(GOODREADS_REVIEW_SPOILERS), 'goodreads_reviews_spoiler_raw.json.gz'),
            'r'
    ) as f:
        for line in f.readlines():
            datum = json.loads(line)
            if datum['rating'] == 0:
                continue

            data.append([
                datum['user_id'],
                datum['book_id'],
                datum['rating'],
                datetime.datetime.strptime(datum['date_added'], '%a %b %d %H:%M:%S %z %Y').timestamp()
            ])

    df = pd.DataFrame(data, columns=['user_id', 'book_id', 'rating', 'timestamp'])
    df['user_id_new'] = df['user_id'].astype('category').cat.rename_categories(range(1, df['user_id'].nunique() + 1))
    df = df[['user_id_new', 'book_id', 'rating', 'timestamp']]
    df.rename(columns={'user_id_new': 'user_id', 'book_id': 'item_id'}, inplace=True)

    df.to_csv(make_ratings_file_path(GOODREADS_REVIEW_SPOILERS),
              sep=',',
              index=None)


def download_and_transform_dataset(dataset_descriptor: DatasetDescriptor, verbose=True):
    """Downloads a dataset by given descriptor.
    Next, transforms it into a CSV file that always contains columns 'user_id', 'item_id', 'rating'. Some additional columns may also
    be presented.
    This file can be found in os.path.join(dataset_descriptor.dir, RATINGS_FILE_NAME)
    """
    # TODO Add format property to DatasetDescriptor
    if dataset_descriptor.url.endswith('.zip'):
        download_and_extract_f = download_and_extract_zip
    elif dataset_descriptor.url.endswith('.gz'):
        download_and_extract_f = download_and_extract_tar
    elif dataset_descriptor.url.startswith('https://drive.google.com'):
        download_and_extract_f = download_and_extract_from_google_drive
    else:
        raise ValueError(f'Unknown archive format at url {dataset_descriptor.url}')

    download_and_extract_f(dataset_descriptor.url, make_dataset_path(dataset_descriptor), verbose=verbose)

    if os.path.exists(make_ratings_file_path(dataset_descriptor)):
        if verbose:
            print(f'Dataset is already transformed, skipped')
    else:
        if dataset_descriptor.id == MOVIELENS_100K.id:
            _transform_movielens_100k()
        elif dataset_descriptor.id == MOVIELENS_1M.id:
            _transform_movielens_1m()
        elif dataset_descriptor.id == MOVIELENS_10M.id:
            _transform_movielens_10m()
        elif dataset_descriptor.id == EPINIONS.id:
            _transform_epinions()
        elif dataset_descriptor.id == LIBRARY_THING.id:
            _transform_library_thing()
        elif dataset_descriptor.id == GOODREADS_REVIEW_SPOILERS.id:
            _transform_goodreads_reviews_spoliers()

    if verbose:
        print(f'Dataset "{dataset_descriptor.name}" is ready for use')
