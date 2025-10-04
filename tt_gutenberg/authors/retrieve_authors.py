import pandas as pd
def get_alias():
    gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    authors_and_aliases = gutenberg_authors[['gutenberg_author_id', 'author', 'alias']]
    return authors_and_aliases.sort_values('gutenberg_author_id', ascending=True)