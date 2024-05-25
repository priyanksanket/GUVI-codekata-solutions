import json
from io import StringIO

def grade_students(scores):
    def get_grade(score):
        #..... YOUR CODE STARTS HERE .....
    
        if score >= 90:
            return 'A'
        elif 80 <= score < 90:
            return 'B'
        elif 70 <= score < 80:
            return 'C'
        elif 60 <= score < 70:
            return 'D'
        else:
            return 'F'    
    
        #..... YOUR CODE ENDS HERE .....
        
    return list(map(get_grade, scores))

if __name__ == "__main__":
    scores = json.load(StringIO(input().strip()))
    grades = grade_students(scores)
    
    print(grades)
