import requests
import json

def BoolReturn(value):
    if value == False:
        return 'false'
    elif value ==True:
        return 'true'

class Subito:
    
    
    def __init__(self, search_item, category = ''):
        
        self.search_item = search_item
        with open('data.json', 'r') as f:
                self.data = json.load(f)
        
        if category == '':
            self.category = ''
        else: 
            self.category = self.data['categories'][category]
            
        
    ## "municipality" code can be found here --> https://dait.interno.gov.it/territorio-e-autonomie-locali/sut/elenco_codici_comuni.php
    ## keep in mind that the municipality has to be located in the declared "region" otherwise it won't return any data
    def search(self, results:int = 100, sort_by:str = "date", ad_type:str = 'for sale',region:str = '',
               title_search:bool = False, shipping:bool = False, municipality = ''):
        
        url = "https://www.subito.it/hades/v1/search/items"
        
        if len(region) == 0 and len(str(municipality)) >0:
            raise ValueError('Please specify the region where the municipality is located')   
        
        sort_by = self.data['sort by'][sort_by.lower()]
        ad_type = self.data['ad type'][ad_type.lower()]
        region = self.data['regions'][region.lower()]
        Title_search = BoolReturn(title_search)
        Shipping = BoolReturn(shipping)
        
        

        i = 100  ## new results
        results_list = []  ## empty list to populate with the results we'll get 
        
        while i <= results: ## the REST API gives maximum 100 results, we need to manipulate the request by using a loop to get more

            j = i-100 ## start search from result in this position
            
            querystring = {"q" : self.search_item, "c": self.category,"r":region,"to":str(municipality),
                           "t":ad_type,"qso":Title_search,"shp":Shipping,"sort":sort_by,"lim":i,"start": j}
            payload = ""
            headers = {"Accept": "application/json, text/plain, */*","X-Subito-Environment-ID": ""}

            response = requests.request("GET", url, data=payload, headers=headers, params=querystring).json()  
            results_list = results_list + response['ads']  ## append the result of each request
            print(querystring)
            i += 100 
                     
        return results_list
            