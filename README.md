# Subito.it-API
Unofficial Wrapper API for the website [@Subito.it](https://www.subito.it/)

## Author
- [@alebrandi](https://www.github.com/alebrandi)

## Description

Unofficial API which scrapes the products on [@Subito.it](https://www.subito.it/) which is kind of the italian version of the website [@Craigslist.org](https://www.craigslist.org/about/sites?lang=en&cc=gb#US)


## Quick Start Guide

```
from subito import Subito


subito.search_item(subito = Subito(search_item = 'fiat 500', category='Auto')

results = subito.search(results = 100, sort_by = "date", ad_type= 'for sale',region = 'lombardia',
               title_search = False, shipping = False, municipality = '015146')

```
More documentation and additional features for the API will be uploaded soon.
