def calculate_interest(principal, rate, time):
    #..... YOUR CODE STARTS HERE .....
    
    monthly_rate = rate / (100 * 12)  # Convert annual rate to monthly rate
    monthly_interest = principal * monthly_rate * time
    return monthly_interest    
    
    #..... YOUR CODE ENDS HERE .....


if __name__ == "__main__":
    principal, rate, time = list(map(float, input().strip().split(',')))
    
    # Calculate and print monthly interest
    print(calculate_interest(principal, rate, time))
