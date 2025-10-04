from .listed import list_authors

__all__ = ['list_authors']


"""
tt_gutenberg.authors package

This package provides functions for accessing and processing Project Gutenberg author data.

Modules
-------
listed
    Contains functions to list authors and compute translation counts, e.g., `list_authors`.

Exports
-------
list_authors : function
    List authors along with their translation counts, optionally returning aliases.
    
Only the listed module is added due to no other module needing to be used outside of this package.
"""