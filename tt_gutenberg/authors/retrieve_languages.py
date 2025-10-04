import pandas as pd
from .retrieve_data import get_gutenberg_data
def count_languages():
    df = get_gutenberg_data()
    names_and_languages = df.groupby(['gutenberg_author_id', 'author'])['language'] \
                            .nunique() \
                            .reset_index()
    names_and_languages = names_and_languages.rename(columns={'language' : 'translation_count'})
    names_and_languages = names_and_languages.sort_values('gutenberg_author_id', ascending=True).reset_index(drop=True)
    return names_and_languages