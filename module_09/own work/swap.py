def swap_numbers():

    num1, num2 = map(int, input("Enter two numbers: ").split())
    

    print(f"Before swapping: num1 = {num1}, num2 = {num2}")
    
    num1, num2 = num2, num1
    
    print(f"After swapping: num1 = {num1}, num2 = {num2}")

swap_numbers()
