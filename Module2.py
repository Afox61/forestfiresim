# This program calculates the square of a number using a function

# Define the function
def square(number):
    """
    This function takes a number as input
    and returns the square of that number.
    """
    return number * number

# Main part of the program
print("Welcome to the Square Calculator!")
num = int(input("Enter a number: "))
result = square(num)  # Bug: Typo in the function name
print(f"The square of {num} is {result}.")
