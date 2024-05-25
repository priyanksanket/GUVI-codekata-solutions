import sys
import json
from io import StringIO

def iterate_students(students):
    #..... YOUR CODE STARTS HERE .....
    
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['course']}, Grade: {student['grade']}")    
    
    #..... YOUR CODE ENDS HERE .....
    
def clean_input(value):
    value = value.strip() 
    if (len(value)):
        if ('}'  not in value):
            value += '}'
        
        if ('{' in value and '}' in value):
            return json.load(StringIO(value))
    return False
    
if __name__ == "__main__":
    students_list = ""

    for line in sys.stdin:
        line = line.strip()
        students_list += line
    
    students_list = list(map(clean_input, students_list.replace('[', '').replace(']', '').split('},')))
    students_list = list(filter(lambda student: isinstance(student, dict), students_list))

    iterate_students(students_list)
