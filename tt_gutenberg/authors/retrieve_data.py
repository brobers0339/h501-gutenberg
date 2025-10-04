import pandas as pd
def get_gutenberg_data():
    gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
    authors_and_languages = gutenberg_metadata[['author', 'language', 'gutenberg_author_id']]
    return authors_and_languages