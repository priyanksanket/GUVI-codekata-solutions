import re

def get_movies(data):
    #..... YOUR CODE STARTS HERE .....
    
    # Define the regular expression pattern
    pattern = r'([\w\s]+) \((\d{4})\)'

    # Find all matches using the pattern
    matches = re.findall(pattern, data)

    # Create a list of tuples from the matches
    movies = [(title.strip(), year) for title, year in matches]

    return movies    
    
    #..... YOUR CODE ENDS HERE .....
    
if __name__ == "__main__":
    data = input().strip()
    print(get_movies(data))
