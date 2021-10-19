import pytest
import os

from drsu.config import DRSUConfiguration
from drsu.datasets import make_dataset_path, make_ratings_file_path, MOVIELENS_100K


def test_local_dir_path(restore_config):
    DRSUConfiguration.local_dataset_dir = 'testdir'

    assert make_dataset_path(MOVIELENS_100K) == os.path.join('testdir', MOVIELENS_100K.dir)


def test_ratings_file_path(restore_config):
    DRSUConfiguration.local_dataset_dir = 'testdir'
    DRSUConfiguration.ratings_file_name = 'testfile.csv'

    assert make_ratings_file_path(MOVIELENS_100K) == os.path.join('testdir', MOVIELENS_100K.dir, 'testfile.csv')
