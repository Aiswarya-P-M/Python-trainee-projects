def factorial(number):
    if number<0:
        return False
    elif number==0:
        return 1
    else:
        return number*factorial(number-1)

number=int(input("Enter a number:"))
print(f" The factorial of {number} is:",factorial(number))