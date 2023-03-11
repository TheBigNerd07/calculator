import time
from calculator_functions import *
def quit_menu():
    print(" ")
    print("Choose an option: ")
    print("1. Basic")
    print("2. Advanced")
    print("3. Stats")
    print("4. Other")
    print("5. Return to menu after calculation")
    print("Type 'Stop' to stop on any menu except during calculations")
    userInput = input("Enter number here: ")
    if userInput == "1":
        quit_basic()
    elif userInput == "2":
        quit_advanced()
    elif userInput == "3":
        quit_stats()
    elif userInput == "4":
        quit_other()
    elif userInput == "5":
        return_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        quit_menu()

def quit_basic():
    print(" ")
    print("Choose an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Main Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
        quit_one_addition()
    elif userInput == "2":
        quit_two_subtraction()
    elif userInput == "3":
        quit_three_multiplication()
    elif userInput == "4":
        quit_four_division()
    elif userInput == "5":
       quit_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        quit_basic()

def quit_advanced():
    print(" ")
    print("Choose an option:")
    print("1. Power")
    print("2. Square Root")
    print("3. Factorial")
    print("4. Absolute Value")
    print("5. Main Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
        quit_one_pow()
    elif userInput == "2":
        quit_two_sqrt()
    elif userInput == "3":
        quit_three_factorial()
    elif userInput == "4":
        quit_four_absolute()
    elif userInput == "5":
        quit_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        quit_advanced()

def quit_stats():
    print(" ")
    print("Choose an option:")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Range")
    print("5. Main Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
        quit_one_mean()
    elif userInput == "2":
        quit_two_median()
    elif userInput == "3":
        quit_three_mode()
    elif userInput == "4":
        quit_four_range()
    elif userInput == "5":
        quit_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        quit_stats()

def quit_other():
    print(" ")
    print("Choose an option:")
    print("1. GCD")
    print("2. LCM")
    print("3. Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
        quit_one_gcd()
    elif userInput == "2":
        quit_two_lcm()
    elif userInput == "3":
        quit_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        quit_other()

def return_menu():
    print(" ")
    print("Choose an option: ")
    print("1. Basic")
    print("2. Advanced")
    print("3. Stats")
    print("4. Other")
    print("5. Quit after calculation")
    print("Type 'Stop' to stop on any menu except during calculations")
    userInput = input("Enter number here: ")
    if userInput == "1":
        return_basic()
    elif userInput == "2":
        return_advanced()
    elif userInput == "3":
        return_stats()
    elif userInput == "4":
        return_other()
    elif userInput == "5":
        quit_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        return_menu()

def return_basic():
    print(" ")
    print("Choose an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Main Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
       return_one_addition()
       return_menu()
    elif userInput == "2":
        return_two_subtraction()
        return_menu()
    elif userInput == "3":
        return_three_multiplication()
        return_menu()
    elif userInput == "4":
        return_four_division()
        return_menu()
    elif userInput == "5":
        return_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        return_basic()

def return_advanced():
    print(" ")
    print("Choose an option:")
    print("1. Power")
    print("2. Square Root")
    print("3. Factorial")
    print("4. Absolute Value")
    print("5. Main Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
        return_one_pow()
        return_menu()
    elif userInput == "2":
       return_two_sqrt()
       return_menu()
    elif userInput == "3":
        return_three_factorial()
        return_menu()
    elif userInput == "4":
        return_four_absolute()
        return_menu()
    elif userInput == "5":
        return_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        return_advanced()

def return_stats():
    print(" ")
    print("Choose an option:")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Range")
    print("5. Main Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
        return_one_mean()
        return_menu()
    elif userInput == "2":
        return_two_median()
        return_menu()
    elif userInput == "3":
        return_three_mode()
        return_menu()
    elif userInput == "4":
        return_four_range()
        return_menu()
    elif userInput == "5":
        return_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        return_stats()

def return_other():
    print(" ")
    print("Choose an option:")
    print("1. GCD")
    print("2. LCM")
    print("3. Menu")
    userInput = input("Enter number here: ")
    if userInput == "1":
        return_one_gcd()
        return_menu()
    elif userInput == "2":
        return_two_lcm()
        return_menu()
    elif userInput == "3":
        return_menu()
    elif userInput == "Stop":
        quit()
    else:
        print("Enter a valid number ")
        time.sleep(2)
        return_other()

if __name__ == "__main__":
    quit_menu()