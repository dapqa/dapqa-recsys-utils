import pytest
import os

from drsu.config import DRSUConfiguration
from drsu.datasets import make_dataset_path, make_ratings_file_path, MOVIELENS_100K


@pytest.fixture(autouse=True)
def restore_config():
    default_local_dataset_dir = DRSUConfiguration.local_dataset_dir
    default_ratings_file_name = DRSUConfiguration.ratings_file_name

    yield

    DRSUConfiguration.local_dataset_dir = default_local_dataset_dir
    DRSUConfiguration.ratings_file_name = default_ratings_file_name


def test_local_dir_path():
    DRSUConfiguration.local_dataset_dir = 'testdir'

    assert make_dataset_path(MOVIELENS_100K) == os.path.join('testdir', MOVIELENS_100K.dir)


def test_ratings_file_path():
    DRSUConfiguration.local_dataset_dir = 'testdir'
    DRSUConfiguration.ratings_file_name = 'testfile.csv'

    assert make_ratings_file_path(MOVIELENS_100K) == os.path.join('testdir', MOVIELENS_100K.dir, 'testfile.csv')
