"""
Module for listing Project Gutenberg authors with translation or book counts.

This module provides the `list_authors` function, which allows you to retrieve a 
list of authors (or their aliases) sorted by either the number of unique languages 
their works have been translated into, or by the total number of books they have
dependent on inputted parameters when the function is called.

Function
---------
list_authors(by_languages=True, alias=True)
    Returns a list of authors or aliases with either translation counts or book counts.
    
    Parameters
    ----------
    by_languages : bool, default True
        If True, the function returns authors sorted by the number of unique languages 
        their works appear in (translation count). If False, it returns authors sorted 
        by the total number of books.
        
    alias : bool, default True
        If True, the function returns author aliases instead of full author names. Only
        includes known aliases within the dataset. If False, it returns the full name.

    Returns
    -------
    list of tuples
        Each tuple contains (alias_or_author, translation_count_or_book_count), sorted 
        in descending order by count.
    
    Different Case Examples
    --------
    # List aliases by translation count
    list_authors(by_languages=True, alias=True)

    # List full author names by translation count
    list_authors(by_languages=True, alias=False)

    # List aliases by number of books
    list_authors(by_languages=False, alias=True)

    # List full author names by number of books
    list_authors(by_languages=False, alias=False)
"""
# Imports
from .retrieve_languages import count_languages
from .retrieve_book_count import count_books
from .retrieve_authors import get_alias
import pandas as pd

# Function
def list_authors(by_languages=True, alias=True):
    if by_languages:
        translation_df = count_languages()    
        if alias:
            aliases = get_alias()
            merged_gutenberg = pd.merge(translation_df, aliases, on='gutenberg_author_id', how='inner')
            merged_gutenberg = merged_gutenberg.dropna() \
                                                .sort_values('translation_count', ascending=False)
            alias_translation_list = list(zip(merged_gutenberg['alias'], merged_gutenberg['translation_count']))
            return alias_translation_list
        else:
            merged_gutenberg = translation_df.sort_values('translation_count', ascending=False)
            author_translation_list = list(zip(merged_gutenberg['author'], merged_gutenberg['translation_count']))
            return author_translation_list
    else:
        book_df = count_books()
        if alias:
            aliases = get_alias()
            merged_gutenberg = pd.merge(book_df, aliases, on='gutenberg_author_id', how='inner')
            merged_gutenberg = merged_gutenberg.dropna() \
                                                .sort_values('book_count', ascending=False)
            alias_book_list = list(zip(merged_gutenberg['alias'], merged_gutenberg['book_count']))
            return alias_book_list
        else:
            merged_gutenberg = book_df.sort_values('book_count', ascending=False)
            author_book_list = list(zip(merged_gutenberg['author'], merged_gutenberg['book_count']))
            return author_book_list


