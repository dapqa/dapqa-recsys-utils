# dapqa-recsys-util

Small util package containing functions for downloading and preparing RecSys datasets.  
All the datasets are downloaded from their original distributions and do not redistributed via this repository.

## Installation

Just use pip (replace `vx.x.x` with needed release version):

```shell
git+https://github.com/dapqa/dapqa-recsys-utils.git@vx.x.x
```

## Usage

Example usage for Movielens 100k dataset (https://grouplens.org/datasets/movielens/100k/):

```python
from drsu.config import DRSUConfiguration
from drsu.datasets import download_and_transform_dataset, as_pandas, as_numpy, MOVIELENS_100K

# Set a directory for storing downloaded data and a prepared dataset's CSV name
# If the target directory does not exist, it will be created automatically
# These values are default, so this part can be skipped
DRSUConfiguration.local_dataset_dir = 'data'
DRSUConfiguration.ratings_file_name = 'prepared-ratings.csv'

# Download Movielens 100k and transform it to common CSV format
# If data are downloaded and transformed already, nothing will happen
download_and_transform_dataset(MOVIELENS_100K)

# Read user_id, item_id, rating from a prepared CSV either as pandas DataFrame or numpy array
data_df = as_pandas(MOVIELENS_100K)
data_arr = as_numpy(MOVIELENS_100K)

# Read all columns from a prepared CSV either as pandas DataFrame or numpy array
data_df_all = as_pandas(MOVIELENS_100K, only_ratings=False)
data_arr_all = as_numpy(MOVIELENS_100K, only_ratings=False)
```