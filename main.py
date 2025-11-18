def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

if __name__ == "__main__":
    print("Hello, Team!")
    # Вызов функции Студента А
    result_mult = multiply(5, 3)
    print(f"Multiply result: {result_mult}")
    # Вызов функции Студента Б
    result_div = divide(10, 2)
    print(f"Divide result: {result_div}")
