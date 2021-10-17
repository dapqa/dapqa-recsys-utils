from ._descriptor_classes import DatasetDescriptor

MOVIELENS_100K = DatasetDescriptor(
    id='ml100k',
    name='Movielens 100k',
    url='http://files.grouplens.org/datasets/movielens/ml-100k.zip',
    dir='movielens-100k',
    n_users=943,
    n_items=1682,
    n_rows=100000,
    max_user_id=943,
    max_item_id=1682
)

MOVIELENS_1M = DatasetDescriptor(
    id='ml1m',
    name='Movielens 1M',
    url='https://files.grouplens.org/datasets/movielens/ml-1m.zip',
    dir='movielens-1m',
    n_users=6040,
    n_items=3706,
    n_rows=1000209,
    max_user_id=6040,
    max_item_id=3952
)

MOVIELENS_10M = DatasetDescriptor(
    id='ml10m',
    name='Movielens 10M',
    url='https://files.grouplens.org/datasets/movielens/ml-10m.zip',
    dir='movielens-10m',
    n_users=69878,
    n_items=10677,
    n_rows=10000054,
    max_user_id=71567,
    max_item_id=65133
)