import art
import os
print(art.logo)

def add(num1,num2):
    return num1 + num2
def substract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2

operator_dict ={
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
}

def calculator():
    continue_cal = True
    first_numb =float(input("What's your first number?: "))

    for i in operator_dict:
        print(i)
    
    while continue_cal:
        operator = input("Pick an Operation: ")
        next_numb = float(input("What is your next number?: "))
        cal_func = operator_dict[operator]
        ans = round(cal_func(first_numb,next_numb),1)
        continue_calc = input(f"Type 'y' to continue calculating with {round(cal_func(first_numb,next_numb),1)}, or type 'n' to start a new calculation.").lower()
        
        if continue_calc == 'y':
             first_numb = ans
                             
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(art.logo)
            calculator()  
           
            
            

calculator()