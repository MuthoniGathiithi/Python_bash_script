num1=input("Enter first number: ")
num2=input("Enter second number: ")

def sum_of_two(num1, num2):
    sum=int(num1) + int(num2)
    
    return sum
total=sum_of_two(num1, num2)
print("The sum of the two numbers is:", total)