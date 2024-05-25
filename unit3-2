import re

def associate_students(names, scores):
    #..... YOUR CODE STARTS HERE .....
    
    return list(zip(names, scores))    
    
    #..... YOUR CODE ENDS HERE .....
    
def clean_input(value):
    value = value.strip()
    return re.sub(r'[^A-Z0-9a-z,]', '', value).split(',')
    
if __name__ == "__main__":
   names, scores = list(map(clean_input, input().strip().split('],')))
   scores = list(map(int, scores))
   print(associate_students(names, scores))
