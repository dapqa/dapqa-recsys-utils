from dataclasses import dataclass


@dataclass
class DatasetDescriptor:
    """Descriptor with basic info about a dataset (but not data itself)"""
    id: str
    name: str
    url: str
    dir: str
    n_users: int
    n_items: int
    n_rows: int
    max_user_id: int
    max_item_id: int