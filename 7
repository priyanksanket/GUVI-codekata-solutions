import json
from io import StringIO
import re

def unique_brands(products):
    #..... YOUR CODE STARTS HERE .....
    
    return sorted({product['brand'] for product in products})    
    
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
    products = convert_to_list_of_dicts(input().strip())
    print(sorted(unique_brands(products)))
