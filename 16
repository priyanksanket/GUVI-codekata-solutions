import time
import re

class MarriageFunction:
    total_duration = 0

    @classmethod
    def do_task(cls, task):
        #..... YOUR CODE STARTS HERE .....
    
        start_time = time.time()
        time.sleep(task[1])
        end_time = time.time()
        duration = end_time - start_time
        cls.total_duration += duration
        print(f"{task[0]} took {round(duration, 2)} seconds")    
    
        #..... YOUR CODE ENDS HERE .....
    
def replace_non_alphanumeric(text, replacement=''):
    return re.sub(r'[^a-zA-Z0-9, ]', replacement, text)
        
def clean_input(value):
    value = replace_non_alphanumeric(value).split(',')
    
    id, price = list(map(lambda x: x.strip(), value))
    
    return (id, int(price))
    
if __name__ == "__main__":
    tasks = input()
    
    tasks = list(map(clean_input, tasks.strip().replace('[', '').replace(']', '').split('),')))
    
    for task in tasks:
       MarriageFunction.do_task(task)
