import math

class ScientificCalculator:
    
    def add(self, x, y):
        """Return the sum of x and y"""
        return x + y
    
    def subtract(self, x, y):
        """Return the difference of x and y"""
        return x - y
    
    def multiply(self, x, y):
        """Return the product of x and y"""
        return x * y
    
    def divide(self, x, y):
        """Return the division of x by y, raise error if y is zero"""
        if y == 0:
            return "Error: Division by zero"
        return x / y
    
    def power(self, x, y):
        """Return x raised to the power of y"""
        return math.pow(x, y)
    
    def square_root(self, x):
        """Return the square root of x"""
        if x <= 0:
            return "Error: Negative input for square root"
        return math.sqrt(x)
    
    def log(self, x):
        """Return the natural logarithm of x"""
        if x <= 0:
            return "Error: Logarithm defined for positive numbers only"
        return math.log(x)
    
    def log10(self, x):
        """Return the base-10 logarithm of x"""
        if x <= 0:
            return "Error: Logarithm defined for positive numbers only"
        return math.log10(x)
    
    def sine(self, x):
        """Return the sine of x (x in degrees)"""
        return math.sin(math.radians(x))
    
    def cosine(self, x):
        """Return the cosine of x (x in degrees)"""
        return math.cos(math.radians(x))
    
    def tangent(self, x):
        """Return the tangent of x (x in degrees)"""
        return math.tan(math.radians(x))
    
    def factorial(self, x):
        """Return the factorial of x"""
        if x < 0:
            return "Error: Factorial of a negative number doesn't exist"
        return math.factorial(x)

def main():
    calc = ScientificCalculator()
    
    print("Scientific Calculator")
    print("Choose the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Natural Logarithm (ln)")
    print("8. Logarithm Base 10")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Factorial")
    
    while True:
        try:
            choice = int(input("Enter choice (1-12): "))
            if choice not in range(1, 13):
                print("Invalid Input, please choose between 1-12.")
                continue

            if choice == 6:
                num1 = float(input("Enter a number: "))
                result = calc.square_root(num1)
            elif choice == 7:
                num1 = float(input("Enter a number: "))
                result = calc.log(num1)
            elif choice == 8:
                num1 = float(input("Enter a number: "))
                result = calc.log10(num1)
            elif choice == 9:
                num1 = float(input("Enter angle in degrees: "))
                result = calc.sine(num1)
            elif choice == 10:
                num1 = float(input("Enter angle in degrees: "))
                result = calc.cosine(num1)
            elif choice == 11:
                num1 = float(input("Enter angle in degrees: "))
                result = calc.tangent(num1)
            elif choice == 12:
                num1 = int(input("Enter an integer: "))
                result = calc.factorial(num1)
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == 1:
                    result = calc.add(num1, num2)
                elif choice == 2:
                    result = calc.subtract(num1, num2)
                elif choice == 3:
                    result = calc.multiply(num1, num2)
                elif choice == 4:
                    result = calc.divide(num1, num2)
                elif choice == 5:
                    result = calc.power(num1, num2)
                    
            print (f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Ask if the user wants to perform another operation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if _name_ == "_main_":
    main()