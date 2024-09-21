import math

operator = ""
num1 = 0
num2 = 0
result = 0

def input_fnum():
    global num1
    while(True):
        num1 = input("first number: ")
        if num1 == "ans":
            try:
                num1 = result
                break
            except:
                num1 = 0
        elif num1 != "ans":
            try:
                num1 = float(num1)
                break
            except:
                print("must be number")

def input_snum():
    global num2
    while(True):
        try:
            num2 = float(input("second number: "))
            break
        except:
            print("must be number")
            continue
                
def input_op():
    global operator
    while(True):
        operator = input("operator[+,-,*,/,root,sqr]: ")
        if operator == "root" or operator == "sqr":
            break
        elif operator == "+" or operator == "-" or operator == "*" or operator == "/":
            input_snum()
            break
        else:
            print("Invalid operator")
                

def add(fn, sn):
    return fn + sn

def subtract(fn, sn):
    return fn - sn

def multiply(fn, sn):
    return fn*sn

def divide(fn, sn):
    return fn / sn

def sqroot(number):
    return math.sqrt(number)

def square(number):
    number**2
        # match operator:
        #     case "+": result = num1 + num2
        #     case "-": result = num1 - num2
        #     case "*": result = num1*num2
        #     case "/": result = num1 / num2
        #     case "root": result = math.sqrt(num1)
        #     case "sqr": result = num1*num1

        # if operator == "root" or operator == "sqr":
        #     print(f"\n{operator}({num1}) = {result}")
        # else:
        #     print(f"\n{num1} {operator} {num2} = {result}")

        # finished = input("finish?[Y/n]")
        # if finished == "Y" or finished == "y":
        #     break