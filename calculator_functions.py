import math
import time
import statistics

def quit_one_addition():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    one_answer = float(userInputA) + float(userInputB)
    print(one_answer)
    time.sleep(2)

def quit_two_subtraction():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    two_answer = float(userInputA) - float(userInputB)
    print(two_answer)
    time.sleep(2)

def quit_three_multiplication():
    userInputA = input("First Factor: ")
    userInputB = input("Second Factor: ")
    three_answer = float(userInputA) * float(userInputB)
    print(three_answer)
    time.sleep(2)

def quit_four_division():
    userInputA = input("Dividend: ")
    userInputB = input("Divsor: ")
    four_answer = float(userInputA) / float(userInputB)
    print(four_answer)
    time.sleep(2)

def quit_one_pow ():
    userInputA = input("Number: ")
    userInputB = input("Raised to: ")
    pow_answer = math.pow(int(userInputA), int(userInputB))
    print(pow_answer)
    time.sleep(2)

def quit_two_sqrt():
    userInputA = input("Number: ")
    sqrt_answer = math.sqrt(userInputA)
    print(sqrt_answer)
    time.sleep(2)

def quit_three_factorial():
    userInputA = input("Number: ")
    factorial_answer = math.factorial(userInputA)
    print(factorial_answer)
    time.sleep(2)

def quit_four_absolute():
    userInputA = input("Number: ")
    absolute_answer = math.fabs(int(userInputA))
    print(absolute_answer)
    time.sleep(2)

def quit_one_mean():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    mean_answer = statistics.mean(userInputM)
    print(mean_answer)
    time.sleep(2)

def quit_two_median():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    median_answer = statistics.median(userInputM)
    print(median_answer)
    time.sleep(2)

def quit_three_mode():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    mode_answer = statistics.mode(userInputM)
    print(mode_answer)
    time.sleep(2)

def quit_four_range():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    range_answer = statistics.range(userInputM)
    print(range_answer)
    time.sleep(2)

def quit_one_gcd():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    gcd_answer = math.gcd(int(userInputA), int(userInputB))
    print(gcd_answer)
    time.sleep(2)

def quit_two_lcm():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    lcm_answer = (math.fabs(int(userInputA) * int(userInputB)) / (math.gcd(int(userInputA), int(userInputB))))
    print(lcm_answer)
    time.sleep(2)

def return_one_addition():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    one_answer = float(userInputA) + float(userInputB)
    print(one_answer)
    time.sleep(2)

def return_two_subtraction():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    two_answer = float(userInputA) - float(userInputB)
    print(two_answer)
    time.sleep(2)

def return_three_multiplication():
    userInputA = input("First Factor: ")
    userInputB = input("Second Factor: ")
    three_answer = float(userInputA) * float(userInputB)
    print(three_answer)
    time.sleep(2)

def return_four_division():
    userInputA = input("Dividend: ")
    userInputB = input("Divsor: ")
    four_answer = float(userInputA) / float(userInputB)
    print(four_answer)
    time.sleep(2)

def return_one_pow ():
    userInputA = input("Number: ")
    userInputB = input("Raised to: ")
    pow_answer = math.pow(int(userInputA), int(userInputB))
    print(pow_answer)
    time.sleep(2)

def return_two_sqrt():
    userInputA = input("Number: ")
    sqrt_answer = math.sqrt(userInputA)
    print(sqrt_answer)
    time.sleep(2)

def return_three_factorial():
    userInputA = input("Number: ")
    factorial_answer = math.factorial(userInputA)
    print(factorial_answer)
    time.sleep(2)

def return_four_absolute():
    userInputA = input("Number: ")
    absolute_answer = math.fabs(int(userInputA))
    print(absolute_answer)
    time.sleep(2)

def return_one_mean():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    mean_answer = statistics.mean(userInputM)
    print(mean_answer)
    time.sleep(2)

def return_two_median():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    median_answer = statistics.median(userInputM)
    print(median_answer)
    time.sleep(2)

def return_three_mode():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    mode_answer = statistics.mode(userInputM)
    print(mode_answer)
    time.sleep(2)

def return_four_range():
    userInput = input("Data set, each # seperated by ', ': ")
    userInputM = userInput.split(", ")
    for i in range(0, len(userInputM)):
        userInputM[i] = float(userInputM[i])
    range_answer = statistics.range(userInputM)
    print(range_answer)
    time.sleep(2)

def return_one_gcd():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    gcd_answer = math.gcd(int(userInputA), int(userInputB))
    print(gcd_answer)
    time.sleep(2)

def return_two_lcm():
    userInputA = input("First Number: ")
    userInputB = input("Second Number: ")
    lcm_answer = (math.fabs(int(userInputA) * int(userInputB)) / (math.gcd(int(userInputA), int(userInputB))))
    print(lcm_answer)
    time.sleep(2)