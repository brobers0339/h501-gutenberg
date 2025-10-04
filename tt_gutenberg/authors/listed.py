from .retrieve_languages import count_languages
from .retrieve_book_count import count_books
from .retrieve_authors import get_alias
import pandas as pd
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


