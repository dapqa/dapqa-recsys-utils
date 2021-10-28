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
    max_item_id=1682,
    rating_scale=(1, 5)
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
    max_item_id=3952,
    rating_scale=(1, 5)
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
    max_item_id=65133,
    rating_scale=(1, 5)
)

# Check https://cseweb.ucsd.edu/~jmcauley/datasets.html#multi_aspect for citation
EPINIONS = DatasetDescriptor(
    id='ep',
    name='epinions',
    url='http://deepyeti.ucsd.edu/jmcauley/datasets/epinions/epinions_data.tar.gz',
    dir='epinions',
    n_users=116260,
    n_items=41269,
    n_rows=188478,
    max_user_id=116260,
    max_item_id=41269,
    rating_scale=(1, 5)
)

# Check https://cseweb.ucsd.edu/~jmcauley/datasets.html#multi_aspect for citation
LIBRARY_THING = DatasetDescriptor(
    id='libt',
    name='LibraryThing',
    url='http://deepyeti.ucsd.edu/jmcauley/datasets/librarything/lthing_data.tar.gz',
    dir='library-thing',
    n_users=70618,
    n_items=385251,
    n_rows=1387125,
    max_user_id=83194,
    max_item_id=506165,
    rating_scale=(1, 5)
)

# Check https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/reviews for citation
GOODREADS_REVIEW_SPOILERS = DatasetDescriptor(
    id='gr_s',
    name='GoodRead Reviews (w/ spoilers)',
    url='https://drive.google.com/uc?id=1NYV4F1WGJg6QbV0rOSXi6Y1gFLwic94a',
    dir='goodreads-review-spoilers',
    n_users=18868,
    n_items=25469,
    n_rows=1330981,
    max_user_id=18868,
    max_item_id=36328685,
    rating_scale=(1, 5)
)

DRUG_RECOMMENDATIONS = DatasetDescriptor(
    id='drug_rec',
    name='Drug Recommendations',
    url='https://www.kaggle.com/subhajournal/drug-recommendations',
    dir='drug-recommendations',
    n_users=708,
    n_items=2637,
    n_rows=53766,
    max_user_id=708,
    max_item_id=2637,
    rating_scale=(1, 10)
)

AMAZON_RATINGS_SOFTWARE = DatasetDescriptor(
    id='amz_software',
    name='Amazon Ratings (Software)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Software.csv',
    dir='amazon-ratings-software',
    n_users=21663,
    n_items=375147,
    n_rows=459436,
    max_user_id=21663,
    max_item_id=375147,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_AMAZON_FASHION = DatasetDescriptor(
    id='amz_amazon_fashion',
    name='Amazon Ratings (Amazon Fashion)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/AMAZON_FASHION.csv',
    dir='amazon-ratings-amazon-fashion',
    n_users=186189,
    n_items=749233,
    n_rows=883636,
    max_user_id=186189,
    max_item_id=749233,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_ALL_BEAUTY = DatasetDescriptor(
    id='amz_all_beauty',
    name='Amazon Ratings (All Beauty)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/All_Beauty.csv',
    dir='amazon-ratings-all-beauty',
    n_users=32586,
    n_items=324038,
    n_rows=371345,
    max_user_id=32586,
    max_item_id=324038,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_APPLIANCES = DatasetDescriptor(
    id='amz_appliances',
    name='Amazon Ratings (Appliances)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Appliances.csv',
    dir='amazon-ratings-appliances',
    n_users=30252,
    n_items=515650,
    n_rows=602777,
    max_user_id=30252,
    max_item_id=515650,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_ARTS_CRAFTS_AND_SEWING = DatasetDescriptor(
    id='amz_arts_crafts_and_sewing',
    name='Amazon Ratings (Arts Craft and Sewing)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Arts_Crafts_and_Sewing.csv',
    dir='amazon-ratings-arts-crafts-and-sewing',
    n_users=302809,
    n_items=1579230,
    n_rows=2875917,
    max_user_id=302809,
    max_item_id=1579230,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_CDS_AND_VINYL = DatasetDescriptor(
    id='amz_cds_and_vinyl',
    name='Amazon Ratings (CDs and Vinyl)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/CDs_and_Vinyl.csv',
    dir='amazon-ratings-cds-and-vinyl',
    n_users=434060,
    n_items=1944316,
    n_rows=4543369,
    max_user_id=434060,
    max_item_id=1944316,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_DIGITAL_MUSIC = DatasetDescriptor(
    id='amz_digital_music',
    name='Amazon Ratings (Digital Music)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Digital_Music.csv',
    dir='amazon-ratings-digital-music',
    n_users=456992,
    n_items=840372,
    n_rows=1584082,
    max_user_id=456992,
    max_item_id=840372,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_GIFT_CARDS = DatasetDescriptor(
    id='amz_gift_cards',
    name='Amazon Ratings (Gift Cards)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Gift_Cards.csv',
    dir='amazon-ratings-gift-cards',
    n_users=1548,
    n_items=128877,
    n_rows=147194,
    max_user_id=1548,
    max_item_id=128877,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_INDUSTRIAL_AND_SCIENTIFIC = DatasetDescriptor(
    id='amz_industrial_and_scientific',
    name='Amazon Ratings (Industrial and Scientific)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Industrial_and_Scientific.csv',
    dir='amazon-ratings-industrial_and_scientific',
    n_users=165764,
    n_items=1246131,
    n_rows=1758333,
    max_user_id=165764,
    max_item_id=1246131,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_LUXURY_BEAUTY = DatasetDescriptor(
    id='amz_luxury_beauty',
    name='Amazon Ratings (Luxury Beauty)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Luxury_Beauty.csv',
    dir='amazon-ratings-luxury-beauty',
    n_users=12120,
    n_items=416174,
    n_rows=574628,
    max_user_id=12120,
    max_item_id=416174,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_MAGAZINE_SUBSCRIPTIONS = DatasetDescriptor(
    id='amz_magazine_subscriptions',
    name='Amazon Ratings (Magazine Subscriptions)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Magazine_Subscriptions.csv',
    dir='amazon-ratings-magazine-subscriptions',
    n_users=2428,
    n_items=72098,
    n_rows=89689,
    max_user_id=2428,
    max_item_id=72098,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_MUSICAL_INSTRUMENTS = DatasetDescriptor(
    id='amz_musical_instruments',
    name='Amazon Ratings (Musical Instruments)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Musical_Instruments.csv',
    dir='amazon-ratings-musical-instruments',
    n_users=112222,
    n_items=903330,
    n_rows=1512530,
    max_user_id=112222,
    max_item_id=903330,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_PRIME_PANTRY = DatasetDescriptor(
    id='amz_prime_pantry',
    name='Amazon Ratings (Prime Pantry)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Prime_Pantry.csv',
    dir='amazon-ratings-prime-pantry',
    n_users=10814,
    n_items=247659,
    n_rows=471614,
    max_user_id=10814,
    max_item_id=247659,
    rating_scale=(1, 5)
)

AMAZON_RATINGS_VIDEO_GAMES = DatasetDescriptor(
    id='amz_video_games',
    name='Amazon Ratings (Video Games)',
    url='http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Video_Games.csv',
    dir='amazon-ratings-video-games',
    n_users=71982,
    n_items=1540618,
    n_rows=2565349,
    max_user_id=71982,
    max_item_id=1540618,
    rating_scale=(1, 5)
)

# ---
ALL_DESCRIPTORS = (
    MOVIELENS_100K,
    MOVIELENS_1M,
    MOVIELENS_10M,
    EPINIONS,
    LIBRARY_THING,
    GOODREADS_REVIEW_SPOILERS,
    AMAZON_RATINGS_SOFTWARE,
    AMAZON_RATINGS_AMAZON_FASHION,
    AMAZON_RATINGS_ALL_BEAUTY,
    AMAZON_RATINGS_APPLIANCES,
    AMAZON_RATINGS_ARTS_CRAFTS_AND_SEWING,
    AMAZON_RATINGS_CDS_AND_VINYL,
    AMAZON_RATINGS_DIGITAL_MUSIC,
    AMAZON_RATINGS_GIFT_CARDS,
    AMAZON_RATINGS_INDUSTRIAL_AND_SCIENTIFIC,
    AMAZON_RATINGS_LUXURY_BEAUTY,
    AMAZON_RATINGS_MAGAZINE_SUBSCRIPTIONS,
    AMAZON_RATINGS_MUSICAL_INSTRUMENTS,
    AMAZON_RATINGS_PRIME_PANTRY,
    AMAZON_RATINGS_VIDEO_GAMES,
)
