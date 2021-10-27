import os
import tarfile
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from drsu.config import DRSUConfiguration
from drsu.datasets import DatasetDescriptor


def make_dataset_path(dataset_descriptor: DatasetDescriptor) -> str:
    return os.path.join(DRSUConfiguration.local_dataset_dir, dataset_descriptor.dir)


def make_ratings_file_path(dataset_descriptor: DatasetDescriptor) -> str:
    return os.path.join(make_dataset_path(dataset_descriptor), DRSUConfiguration.ratings_file_name)


def download_and_extract_zip(url, output_dir_name, verbose=True):
    """Downloads a zip file from given url and extracts it into given output directory.
    If the output dir already exists, does nothing.
    """
    if os.path.exists(output_dir_name):
        if verbose:
            print(f'{output_dir_name} already exists, skipped')
        return

    with urlopen(url) as zip_response:
        with ZipFile(BytesIO(zip_response.read())) as zip_file:
            zip_file.extractall(output_dir_name)

    if verbose:
        print(f'Zip file from {url} has been extracted to {output_dir_name}')


def download_and_extract_tar(url, output_dir_name, verbose=True):
    if os.path.exists(output_dir_name):
        if verbose:
            print(f'{output_dir_name} already exists, skipped')
        return

    with urlopen(url) as tar_response:
        with tarfile.open(fileobj=BytesIO(tar_response.read())) as tar_file:
            tar_file.extractall(output_dir_name)

    if verbose:
        print(f'Tar file from {url} has been extracted to {output_dir_name}')
