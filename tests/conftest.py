import pytest

from drsu.config import DRSUConfiguration


def pytest_addoption(parser):
    extra_options = {
        "skip_datasets": "List of ids of datasets which tests must be skipped"
    }

    for option, description in extra_options.items():
        parser.addini(option, description)
        parser.addoption(f'--{option}', help=description)


@pytest.fixture
def restore_config():
    default_local_dataset_dir = DRSUConfiguration.local_dataset_dir
    default_ratings_file_name = DRSUConfiguration.ratings_file_name

    yield

    DRSUConfiguration.local_dataset_dir = default_local_dataset_dir
    DRSUConfiguration.ratings_file_name = default_ratings_file_name
