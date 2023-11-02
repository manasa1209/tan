# """
# This is a Python script that does the simple operations of the calculator.
# """

# class Calculator:
#     def add(self, x, y):
#         return x + y
    
#     def subtract(self, x, y):
#         return x - y
    
#     def multiply(self, x, y):
#         return x * y
    
#     def divide(self, x, y):
#         if y == 0:
#             raise ValueError("Division by zero is not allowed")
#         return x / y

"""
This is a Python script that provides simple calculator operations.
"""

class Calculator:
    @staticmethod
    def add(x, y):
        """
        Adds two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The sum of x and y.
        """
        return x + y
    
    @staticmethod
    def subtract(x, y):
        """
        Subtracts one number from another.

        :param x: The number to subtract from.
        :param y: The number to subtract.
        :return: The result of x - y.
        """
        return x - y
    
    @staticmethod
    def multiply(x, y):
        """
        Multiplies two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The product of x and y.
        """
        return x * y
    
    @staticmethod
    def divide(x, y):
        """
        Divides one number by another.

        :param x: The dividend.
        :param y: The divisor.
        :return: The result of x / y.
        :raises ValueError: If division by zero is attempted.
        """
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y
