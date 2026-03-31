# Improved example demonstrating *args and **kwargs with best practices

def add(*numbers):
    """Returns the sum of any number of positional arguments."""
    return sum(numbers)   # Cleaner and Pythonic


def calculate(n, **operations):
    """Applies operations to n based on provided keyword arguments."""
    # Safely extract values with defaults
    add_value = operations.get("add", 0)
    multiply_value = operations.get("multiply", 1)

    n += add_value
    n *= multiply_value

    return n


# Example usage
result_sum = add(3, 5, 6, 2, 1, 7, 4, 3)
print("Sum:", result_sum)

result_calc = calculate(2, add=3, multiply=5)
print("Calculate Result:", result_calc)



# Improved Car class using kwargs smartly
class Car:
    def __init__(self, **info):
        """Dynamically assigns attributes from kwargs."""
        for key, value in info.items():
            setattr(self, key, value)  # Automatically becomes a class attribute

    def __str__(self):
        return f"Car(make={getattr(self, 'make', None)}, model={getattr(self, 'model', None)})"


my_car = Car(make="Nissan", model="Skyline", colour="Blue")
print(my_car.model)
print(my_car)