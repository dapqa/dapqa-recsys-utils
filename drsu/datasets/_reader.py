import numpy as np
import pandas as pd

from drsu.datasets import DatasetDescriptor
from drsu.datasets._utils import make_ratings_file_path


def as_pandas(dataset_descriptor: DatasetDescriptor, only_ratings=True) -> pd.DataFrame:
    full_df = pd.read_csv(make_ratings_file_path(dataset_descriptor), sep=',')
    if only_ratings:
        return full_df[['user_id', 'item_id', 'rating']]
    else:
        return full_df


def as_numpy(dataset_descriptor: DatasetDescriptor, only_ratings=True) -> np.ndarray:
    df = as_pandas(dataset_descriptor, only_ratings)
    return df.to_numpy()