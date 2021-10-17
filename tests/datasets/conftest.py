import pytest

from drsu.config import DRSUConfiguration


@pytest.fixture(autouse=True)
def restore_config():
    default_local_dataset_dir = DRSUConfiguration.local_dataset_dir
    default_ratings_file_name = DRSUConfiguration.ratings_file_name

    yield

    DRSUConfiguration.local_dataset_dir = default_local_dataset_dir
    DRSUConfiguration.ratings_file_name = default_ratings_file_name
