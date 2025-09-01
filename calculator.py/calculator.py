def add(a:int,b:int):
    return a + b
def subtract(a:int,b:int):
    return a - b
try:
    operation = input("Enter the operation you want to perform (add/subtract): ").strip().lower()
    if operation not in ['add', 'subtract']:
        raise ValueError("Invalid operation. Please enter 'add' or 'subtract'.")  
    if operation == 'add':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(add(a,b))
    elif operation == 'subtract':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(subtract(a,b))
except ValueError as e:
    print(f"Error: {e}")
print("Oop")