import os
import time


def print_arrow_Right(n):
    for i in range(6):
        print("\n")
    for i in range(n):
        print("                           ", end="")
        for j in range(i+1):
            print("*", end="")
        print()
    print("                    ", end="")
    print("***************")
    for i in range(n, 0, -1):
        print("                           ", end="")
        for j in range(i):
            print("*", end="")
        print()
# print_arrow_Right(5)


def print_arrow_left(n):
    for i in range(6):
        print("\n")
    for i in range(n):
        print("        ", end="")
        for j in range(n):
            if j >= n-i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("     ", end="")
    print("***************")
    for i in range(n, 0, -1):
        print("        ", end="")
        for j in range(n):
            if j >= n-i:
                print("", end="")
                print("*", end="")
            else:
                print(" ", end="")
        print()
# print_arrow_left(5)


def print_arrow_lower(n):
    for i in range(12):
        print("\n")
    for i in range(n):
        print("               ", end="")
        for j in range(n):
            if j == n-3:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n, 0, -2):
        print("             ", end="")
        for j in range(n-1):
            if j >= n-i:
                print(" ", end="")
                print("*", end="")
            else:
                print(" ", end="")
        print()
# print_arrow_lower(8)


def print_arrow_uper(n):
    for i in range(n+1, 0, -2):
        print("            ", end="")
        for j in range(n):
            if j >= i:
                print(" ", end="")
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n):
        print("               ", end="")
        for j in range(n):
            if j == n-3:
                print("*", end="")
            else:
                print(" ", end="")
        print()
 # print_arrow_uper(8)


while True:
    print_arrow_Right(5)
    # Wait for .3 seconds
    time.sleep(.3)
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    print_arrow_uper(5)
    time.sleep(.3)
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    print_arrow_left(5)
    time.sleep(.3)
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    print_arrow_lower(5)
    time.sleep(.3)
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
