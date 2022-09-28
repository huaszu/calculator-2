"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
allowed_operators = ["+", "-", "*", "/", "sq", "cube", "pow", "mod"]

while True:
    equation = input("Enter your equation: ")
    tokens = equation.split(" ")
    operator = tokens[0]
    
    # result = None

    if operator == "q":
        break
                
    else:
        if len(tokens) < 2:
            print("Warning: Not enough inputs.")
            continue
        elif operator not in allowed_operators:
            print("Please only use allowed operators")
            continue
        try:
            num1 = float(tokens[1])
            # len(tokens) > 1 
        except (ValueError, NameError) as error:
            print(error)
            #print("Please only give numbers as operands and only use allowed operators")
            continue
            
        if operator == "sq":
            result = square(num1)
            print(result)
            
        elif operator == "cube":
            result = cube(num1)
            print(result)

        else:
            if len(tokens) < 3:
                num2 = "0"

            else:
                num2 = tokens[2]
            # try:
            #     num2 = float(tokens[2])
            # except:
            #     print("Please only give numbers as operands")
            #     continue

            if operator == "+":
                result = add(num1, num2)
                print(result)
            elif operator == "-":
                result = subtract(num1, num2)
                print(result)
            elif operator == "*":
                result = multiply(num1, num2)
                print(result)
            elif operator == "/":
                result = divide(num1, num2)
                print(result)
            elif operator == "pow":
                result = power(num1, num2)
                print(result)
            elif operator == "mod":
                result = mod(num1, num2)
                print(result)