numbers=[90,100]

def sum_of_list(numbers):
  total=0
  for i in numbers:
      total= total + i
  return total
result=sum_of_list(numbers)
print("The sum of the list is:", result)