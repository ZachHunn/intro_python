

# function
def print_menu():
    print("_" * 20)
    print("Pyton Calc")
    print("_" * 20)

    print("[1]- Add")
    print("[2]- Subtract")
    print("[3]- Multiple")
    print("[4]- Divide")
    print("[x]- Close app")

def addition (a, b):
   total = a + b
   print(f" \n {a} + {b} = {total}")

def sub(a,b):
    total = a - b
    print( f"{a} - {b} = {total}")

def multiple(a,b):
   total = a * b
   print( f" {a} * {b} = {total} ")

def divide(a,b):
    if (a or b == 0):
        
        total = a / b
        print( f" {a} / {b} = {total} ")

"""
option ask for the year of birth and tell the age
"""
#instructions
op = ""

while (op != "x"):
    print_menu()
    op = input("Please choose an option: ")
    
    if (op != "x"):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter your second number: "))

    if (op == "1"):
        addition(num1,num2)
    elif(op == "2"):
        sub(num1, num2)
    elif(op == "3"):
        multiple(num1,num2)
    elif(op == "4"):
        divide(num1, num2)
print("\n\nGood Bye")
   
