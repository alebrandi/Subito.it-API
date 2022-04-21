# Subito.it-API
Unofficial Wrapper API for the website [Subito.it](https://www.subito.it/)

## Author
- [@alebrandi](https://www.github.com/alebrandi)

## Description

Unofficial API which scrapes the products on [Subito.it](https://www.subito.it/) which is kind of the italian version of the website [Craigslist.org](https://www.craigslist.org/about/sites?lang=en&cc=gb#US)


## Quick Start Guide

```
from subito import Subito


subito = Subito(search_item = 'fiat 500', category='Auto')

results = subito.search(results = 100, sort_by = "date", ad_type= 'for sale',region = 'lombardia',
               title_search = False, shipping = False, municipality = '015146')

```

The Subito class takes 2 parameters:
- search_item (string): represents the item you want to search on the website.
- category (string): represents the category in which you want to look for the item. 
                     Not declaring this parameter will result in a search throughout the entire website.
                     The correct category can be found in the data.json file.

The search() method takes 7 parameters:
- results (int): maximum number of results you want back. Defaults to 100 results. Declaring less than 100 results will return 0 results
- sort_by (string): you can sort the results by: -most recent (sort_by = "date")
                                                -lowest price (sort_by = "lowest price")
                                                -highest price (sort_by = "highest price"). It defaults to lowest price.
- ad_type (string): returns either "for sale" (ad_type = "for sale") or "wanted" (ad_type = "wanted") ads. Defaults to "for sale"
- region (string) : returns ads located in a specific region of Italy. The region name has to be declared using the italian name.
                    Defaults to no particular region specified.
- municipality (string) : returns ads located in a specific municipality of the region.
                    Defaults to no particular municipality specified.
                    Must input the ISTAT CODE for the municipality. It can be found [here](https://dait.interno.gov.it/territorio-e-autonomie-locali/sut/elenco_codici_comuni.php) by copying the "CODICE ISTAT" associated with the desired municipality.
                    If the municipality is not located in the declared region, the method will return 0 results.
- title_search (boolean) : if "True" returns only results which have the "search_item" string declared in the class inside the title of the ad.
                           Defaults to False.
- shipping (boolean): if "True" returns only ads whose items can be shipped.
                      Defaults to False


The search() method returns a list of json objects.


More documentation and additional features for the API will be uploaded soon.
