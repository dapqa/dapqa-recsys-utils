import os

import pytest
import tempfile

from drsu.config import DRSUConfiguration
from drsu.datasets import download_and_transform_dataset, make_ratings_file_path, as_pandas, \
    MOVIELENS_100K, MOVIELENS_1M, MOVIELENS_10M


@pytest.fixture(autouse=True, scope='module')
def temp_dir_fixture():
    default_local_dataset_dir = DRSUConfiguration.local_dataset_dir

    temp_dir = tempfile.TemporaryDirectory()
    DRSUConfiguration.local_dataset_dir = temp_dir.name

    yield temp_dir.name

    temp_dir.cleanup()
    DRSUConfiguration.local_dataset_dir = default_local_dataset_dir


@pytest.fixture()
def is_skipped_dataset_fixture(request):
    skip_datasets_str = request.config.getoption("skip_datasets")

    if skip_datasets_str is None:
        try:
            skip_datasets_str = request.config.getini("skip_datasets")
        except ValueError:
            skip_datasets_str = ""

    skip_datasets = set(filter(lambda x: x, [ds_id.strip() for ds_id in skip_datasets_str.split(",")]))
    return lambda dataset_descriptor: dataset_descriptor.id in skip_datasets


@pytest.mark.parametrize("dataset_descriptor", [MOVIELENS_100K, MOVIELENS_1M, MOVIELENS_10M])
def test_movielens(dataset_descriptor, is_skipped_dataset_fixture):
    if is_skipped_dataset_fixture(dataset_descriptor):
        pytest.skip(f'Tests for {dataset_descriptor.name} are skipped')

    download_and_transform_dataset(dataset_descriptor, verbose=False)

    assert os.path.exists(make_ratings_file_path(dataset_descriptor))

    data = as_pandas(dataset_descriptor, only_ratings=False)

    assert (data.columns == ['user_id', 'item_id', 'rating', 'timestamp']).all()
    assert len(data) == dataset_descriptor.n_rows

    user_ids_un = data['user_id'].unique()
    item_ids_un = data['item_id'].unique()

    assert len(user_ids_un) == dataset_descriptor.n_users
    assert len(item_ids_un) == dataset_descriptor.n_items
    assert user_ids_un.max() == dataset_descriptor.max_user_id
    assert item_ids_un.max() == dataset_descriptor.max_item_id


def test_only_ratings_flag(is_skipped_dataset_fixture):
    if is_skipped_dataset_fixture(MOVIELENS_100K):
        pytest.skip(f'Tests for {MOVIELENS_100K.name} are skipped, so test_only_ratings_flag is skipped too')

    download_and_transform_dataset(MOVIELENS_100K, verbose=False)

    data = as_pandas(MOVIELENS_100K, only_ratings=False)
    data_only_ratings = as_pandas(MOVIELENS_100K)

    assert len(data) == len(data_only_ratings)
    assert (data_only_ratings.columns == ['user_id', 'item_id', 'rating']).all()
