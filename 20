class Calculator:
    @staticmethod
    def add(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
        return num1 + num2    
    
        #..... YOUR CODE ENDS HERE .....

    @staticmethod
    def subtract(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
        return num1 - num2    
    
        #..... YOUR CODE ENDS HERE .....

    @staticmethod
    def multiply(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
        return num1 * num2    
    
        #..... YOUR CODE ENDS HERE .....

    @staticmethod
    def divide(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")    
    
        #..... YOUR CODE ENDS HERE .....
            
def call_func(func, args):
    value = None
    num1, num2 = args
    
    if (func == "add"):
        value = Calculator.add(num1, num2)
        
    elif (func == "subtract"):
        value = Calculator.subtract(num1, num2)
    
    elif (func == "multiply"):
        value = Calculator.multiply(num1, num2)
        
    elif (func == "divide"):
        value = Calculator.divide(num1, num2)
        
    return value
    
    
if __name__ == "__main__":
    func_call = list(map(lambda x: str(x.strip()), input().strip().split('.')))
    class_name, func = func_call
    
    if (class_name == 'Calculator'):
        parans_pos = func.index('(')
        
        name = func[:parans_pos].strip()
        args = tuple(map(lambda x: int(x.strip()), func[parans_pos+1: len(func)-1].strip().split(',')))
        
        print(call_func(name, args))
