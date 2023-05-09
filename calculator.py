import math

# Define functions for each operation in standard mode
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

# Define functions for each operation in programmer mode
def bitwise_and(x, y):
    return x & y

def bitwise_or(x, y):
    return x | y

def bitwise_xor(x, y):
    return x ^ y

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def hex_to_binary(hex_num):
    return bin(int(hex_num, 16))[2:].zfill(8)

def binary_to_hex(binary):
    return hex(int(binary, 2))[2:].zfill(2)

def hex_to_decimal(hex_num):
    return int(hex_num, 16)

def decimal_to_hex(decimal):
    return hex(decimal)[2:]

# Prompt user for input
print("Select mode.")
print("1. scintific")
print("2. Programmer")

# Get input from user
mode_choice = input("Enter mode choice (1 or 2): ")

if mode_choice == '1':
    # Prompt user for input in standard mode
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")

    # Get input from user
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    elif choice == '6':
        num1 = float(input("Enter number: "))

    # Perform selected operation
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "**", num2, "=", power(num1, num2))
    elif choice == '6':
        print("sqrt({}) = {}".format(num1, square_root(num1)))
    else:
        print("Invalid input")

elif mode_choice == '2':
    # Prompt user for input in programmer mode
    print("Select operation.")
    print("1. Bitwise AND")
    print("2. Bitwise OR")
    print("3. Bitwise XOR")
    print("4. Binary to Decimal")
    print("5. Decimal to Binary")
    print("6. Hex to Binary")
    print("7. Binary to Hex")
    print("8. Hex to Decimal")
    print("9. Decimal to Hex")
    
    # Get input from user
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice in ['1', '2', '3']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    elif choice == '4':
        binary = input("Enter binary number: ")

    elif choice == '5':
        decimal = int(input("Enter decimal number: "))

    elif choice == '6':
        hex_num = input("Enter hexadecimal number: ")

    elif choice == '7':
        binary = input("Enter binary number: ")

    elif choice == '8':
        hex_num = input("Enter hexadecimal number: ")

    elif choice == '9':
        decimal = int(input("Enter decimal number: "))

    # Perform selected operation
    if choice == '1':
        print(num1, "&", num2, "=", bitwise_and(num1, num2))
    elif choice == '2':
        print(num1, "|", num2, "=", bitwise_or(num1, num2))
    elif choice == '3':
        print(num1, "^", num2, "=", bitwise_xor(num1, num2))
    elif choice == '4':
        print(binary, "in decimal is", binary_to_decimal(binary))
    elif choice == '5':
        print(decimal, "in binary is", decimal_to_binary(decimal))
    elif choice == '6':
        print(hex_num, "in binary is", hex_to_binary(hex_num))
    elif choice == '7':
        print(binary, "in hexadecimal is", binary_to_hex(binary))
    elif choice == '8':
        print(hex_num, "in decimal is", hex_to_decimal(hex_num))
    elif choice == '9':
        print(decimal, "in hexadecimal is", decimal_to_hex(decimal))
    else:
        print("Invalid input")

else:
    print("Invalid input")