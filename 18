from typing import Callable

def calculate(operation: Callable[[float, float], float], num1: float, num2: float) -> float:
    #..... YOUR CODE STARTS HERE .....
    
    return operation(num1, num2)    
    
    #..... YOUR CODE ENDS HERE .....
    
def clean_input(value):
    return str(value.strip())

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else None


operation, num1, num2 = map(clean_input, input().strip().split(','))

func = None

if (operation == 'add'):
    func = add
    
elif (operation == 'subtract'):
    func = subtract
    
elif (operation == 'multiply'):
    func = multiply
    
elif (operation == 'divide'):
    func = divide

print(calculate(func, float(num1), float(num2)))
