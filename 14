import re

def get_products_in_budget(budget, products):
    #..... YOUR CODE STARTS HERE .....
    
    products.sort(key=lambda x: x[1])
    
    total_price = 0
    
    # Yield products one by one until total price exceeds budget
    for product_id, price in products:
        if total_price + price <= budget:
            yield product_id, price
            total_price += price
        else:
            break    
    
    #..... YOUR CODE ENDS HERE .....
        
def replace_non_alphanumeric(text, replacement=''):
    return re.sub(r'[^a-zA-Z0-9,]', replacement, text)
        
def clean_input(value):
    value = replace_non_alphanumeric(value).split(',')
    
    id, price = list(map(lambda x: x.strip(), value))
    
    return (id, int(price))
    
if __name__ == "__main__":
    budget = int(input())
    products = input()
    
    products = list(map(clean_input, products.strip().replace('[', '').replace(']', '').split('),')))
    
    for product in get_products_in_budget(budget, products):
        print(product)
