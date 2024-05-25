class StudentNotFoundError(Exception):
    pass

def get_student_grade(student_id):
    
    students = {
        "BT202101": "A",
        "BT202102": "B",
    }
    if student_id in students:
        return students[student_id]
    else:
        raise StudentNotFoundError("Student not found")

def proxy_get_student_grade(student_id):
    #..... YOUR CODE STARTS HERE .....
    
    try:
        return get_student_grade(student_id)
    except StudentNotFoundError:
        return 'N/A'    
    
    #..... YOUR CODE ENDS HERE .....
        
student_id = input()

print(proxy_get_student_grade(student_id))
