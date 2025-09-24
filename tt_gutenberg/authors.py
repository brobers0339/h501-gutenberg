import authors

import authors.retrieve_authors
import authors.retrieve_data

data = authors.retrieve_data.get_data()
print(authors.retrieve_authors.retrieve_authors(data))

def list_authors(by_languages=True, alias=True):
    return 0
    