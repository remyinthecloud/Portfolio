#Calculator 
import os

#Add
def add(n1, n2):
  return n1+n2

#Subtract
def substract(n1, n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

num1 = int(input("What is the first number?: "))

for operation in operations:
  print(operation)
  
continue_calculation = True
while continue_calculation:
  operation_symbol = input("Pick an operation: ")
  num2 = int(input("What is the next number?: "))
  calculated = operations[operation_symbol]
  answer = calculated(num1, num2)
  print(f"\n{num1} {operation_symbol} {num2} = {answer}")
  
  should_continue = input(f"\nType 'Y' to continue calulating with {answer} or 'N' to start a new calulation or 'E' to exit: ").lower()
  if should_continue == 'y':
    num1 = answer
  elif should_continue == 'n':
    os.system("clear")
    num1 = int(input("What is the first number?: "))
    for operation in operations:
      print(operation)
  elif should_continue == 'e':
    continue_calculation = False
    print("That was fun! Goodbye")
  else:
    print("Invalid input")
    continue_calculation = False
    
 