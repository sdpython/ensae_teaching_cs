"""
@file
@brief shortcuts for data
"""

from .crypt_helper import encrypt_data, decrypt_data
from .data1a import marathon, donnees_enquete_2003_television
from .data2a import wines_quality
from .data_shape_files import data_shape_files, load_french_departments
from .data_irep import load_irep
from .datasql import simple_database
from .datatext import load_sentiment_dataset
from .data_ts import generate_sells
from .dataweb import google_trends, twitter_zip
from .datazips import besancon_df, added, deal_flow_espace_vert_2018_2019
from .gutenberg import gutenberg_name
from .imagenet_classes import interpret_imagenet_results
