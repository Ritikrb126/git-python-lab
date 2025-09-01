def add(a:int,b:int):
    return a + b
try:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    print(add(a,b))
except ValueError:
    print("Entered Invalid input , Only Intergers Allowed")

