num=input("Enter a number: ")

def odd_even(num):
    if int(num) % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = odd_even(num)
print("the number is:", result )