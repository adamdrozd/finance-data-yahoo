import requests

class YahooSearch:

    @staticmethod
    def get_by_isin(search_string: str):
    
        print("calling get isin")

        if search_string == '':
            return ''

        url = "https://query1.finance.yahoo.com/v1/finance/search?q=bob&newsCount=0&listsCount=0"
            
        #url = "https://query1.finance.yahoo.com/v1/finance/search"
        #params = {'q': search_string, 'quotesCount': 1, 'newsCount': 0}

       # r = requests.get(url, params=params)
        r = requests.get(url)

        if r.status_code != 200:
            print("error {}".format(r.status_code))
            return {}

        data = r.json()

        print (data)

        return data