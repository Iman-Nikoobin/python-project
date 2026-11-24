num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, **, %, //, sqrt): ")
if operator in ["+", "-", "*", "/", "**", "%", "//"]:
    num2 = float(input("Enter second number: "))
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    case "**":
        result = num1 ** num2
    case "%":
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Error: Division by zero"
    case "//":
        if num2 != 0:
            result = num1 // num2
        else:
            result = "Error: Division by zero"
    case "sqrt":
        if num1 >= 0:
            result = num1 ** 0.5
        else:
            result = "Error: Negative number"
    case _:
        result = "Invalid operator"
print("Result:", result)