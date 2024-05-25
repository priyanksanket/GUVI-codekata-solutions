import json
from io import StringIO
import re
from math import fsum

def total_price(products, category):
    #..... YOUR CODE STARTS HERE .....
    
    return fsum(product['price'] for product in products if product['category'] == category)    
    
    #..... YOUR CODE ENDS HERE .....
    
def convert_to_list_of_dicts(data):
    data_without_brackets = re.sub(r'[\[\]]', '', data).split('},')
    
    lst = []
    
    data = [d + '}' if '}' not in d else d for d in data_without_brackets]

    for d in data:
        if ('{' in d and '}' in d):
            d = d.strip().replace("'", '"')
            lst.append(json.load(StringIO(d)))
        
    return lst
    
if __name__ == "__main__":
    ip = input().strip().replace("],", ']<DIVIDE>')
    products, category = ip.split("<DIVIDE>")
    products = convert_to_list_of_dicts(products)
    category = category.replace("'", '').strip()
    
    print(total_price(products, category))
