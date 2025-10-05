"""
Module to get the Project Gutenberg data from the metadata csv.

This module reads the csv for the gutenberg metadata from the raw csv link
and returns the data.

Functions
---------
get_gutenberg_data
    Returns a DataFrame with all of the gutenberg metadata
"""
# Import
import pandas as pd

# Function
def get_gutenberg_data():
    gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
    return gutenberg_metadata