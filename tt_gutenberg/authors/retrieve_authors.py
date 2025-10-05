"""
Module to retrieve author aliases.

This module provides the `get_alias` function, which loads the Gutenberg authors dataset 
from the online TidyTuesday CSV, selects relevant columns (author, alias, and author id), 
and returns a DataFrame containing author IDs, full author names, and aliases sorted by author ID.

Functions
---------
get_alias()
    Load the Gutenberg authors dataset and return a DataFrame with the columns:
    'gutenberg_author_id', 'author', and 'alias', sorted by 'gutenberg_author_id'.

"""
# Import
import pandas as pd

# Function
def get_alias():
    gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    authors_and_aliases = gutenberg_authors[['gutenberg_author_id', 'author', 'alias']]
    return authors_and_aliases.sort_values('gutenberg_author_id', ascending=True)