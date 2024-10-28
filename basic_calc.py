import os
# python clear concole function cls()
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

logo = """
 _____________________
|  _________________  |
| |  Sangit's Calc  | |   
| |_________________| |  
|  ___ ___ ___   ___  |  
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| |  
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| | 
| | . | 0 | = | | / | | 
| |___|___|___| |___| | 
|_____________________|
"""



# creating a recursive function so that when the calculation ends it can
# go back to the first stage
def calc():
    print(logo)
    keep_continuing = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
      print(symbol)
    
    while keep_continuing is True:
        operation_symbol = input("Pick an operation: ") 
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        answer = float(answer)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        c = input(f"Press 'y' to Continue with {answer}, or 'n' to abort: ")
        if c == "y":
            num1 = answer
        else:
            keep_continuing = False
            cls()
            calc() 
            # calling this function if done with calculation takes us to first step of entering numbers
    
     
calc()
