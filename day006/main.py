# introduction to functions
# This is a simple Python program that demonstrates how to define and call functions.   
# It includes a function to greet the user and another function to calculate the sum of two numbers.

def greet_user(name):
    """Function to greet the user."""
    print(f"Hello, {name}! Welcome to the Python program.")
def calculate_sum(a, b):
    """Function to calculate the sum of two numbers."""
    return a + b
def main():
    
    """Main function to execute the program."""
    user_name = input("Enter your name: ")
    greet_user(user_name)
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))    
    result = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
if __name__ == "__main__":
    main()
    
# This code defines a simple Python program that demonstrates how to define and call functions.
# It includes a function to greet the user and another function to calculate the sum of two numbers