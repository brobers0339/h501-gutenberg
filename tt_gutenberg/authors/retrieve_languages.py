"""
Module to count the number of languages/translations per author.

This module provides the `count_languages` function, which retrieves the Gutenberg dataset
via `get_gutenberg_data`, groups the data by author and author id, counts the number of unique languages 
per author, and returns a DataFrame sorted by Gutenberg author ID.

Functions
---------
count_languages()
    Returns a DataFrame with columns:
        - 'gutenberg_author_id': the unique ID of the author
        - 'author': the full name of the author
        - 'translation_count': the number of unique languages (translations) by that author
"""
import pandas as pd
from .retrieve_data import get_gutenberg_data
def count_languages():
    df = get_gutenberg_data()
    names_and_languages = df[['gutenberg_author_id', 'author', 'language']]
    names_and_languages = df.groupby(['gutenberg_author_id', 'author'])['language'] \
                            .nunique() \
                            .reset_index()
    names_and_languages = names_and_languages.rename(columns={'language' : 'translation_count'})
    names_and_languages = names_and_languages.sort_values('gutenberg_author_id', ascending=True).reset_index(drop=True)
    return names_and_languages