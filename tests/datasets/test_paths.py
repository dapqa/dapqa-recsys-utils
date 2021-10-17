from drsu.config import DRSUConfiguration


def test1():
    DRSUConfiguration.local_dataset_dir = 'kek'
    assert DRSUConfiguration.local_dataset_dir == 'kek'


def test2():
    assert DRSUConfiguration.local_dataset_dir == 'data'
