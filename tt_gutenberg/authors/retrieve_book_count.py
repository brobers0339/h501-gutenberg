import pandas as pd
from .retrieve_data import get_gutenberg_data
def count_books():
    df = get_gutenberg_data()
    names_and_books = df[['gutenberg_author_id', 'author', 'title']]
    names_and_books = df.groupby(['gutenberg_author_id', 'author'])['title'] \
                            .nunique() \
                            .reset_index()
    names_and_books = names_and_books.rename(columns={'title' : 'book_count'})
    names_and_books = names_and_books.sort_values('gutenberg_author_id', ascending=True).reset_index(drop=True)
    return names_and_books