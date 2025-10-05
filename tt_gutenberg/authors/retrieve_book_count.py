"""
Module to count the number of books per author.

This module provides the `count_books` function, which retrieves the Gutenberg dataset
via `get_gutenberg_data`, groups the data by author, counts the number of unique books 
per author, and returns a DataFrame sorted by Gutenberg author ID.

Functions
---------
count_books()
    Returns a DataFrame with columns:
        - 'gutenberg_author_id': the unique ID of the author
        - 'author': the full name of the author
        - 'book_count': the number of unique books by that author
"""
# Imports
import pandas as pd
from .retrieve_data import get_gutenberg_data

# Function
def count_books():
    df = get_gutenberg_data()
    names_and_books = df[['gutenberg_author_id', 'author', 'title']]
    names_and_books = df.groupby(['gutenberg_author_id', 'author'])['title'] \
                            .nunique() \
                            .reset_index()
    names_and_books = names_and_books.rename(columns={'title' : 'book_count'})
    names_and_books = names_and_books.sort_values('gutenberg_author_id', ascending=True).reset_index(drop=True)
    return names_and_books