radius=input("enter the radius of the circle:")

def area_circle(radius):
    area=3.14 * radius ** 2
    return area
result =area_circle(int(radius))
print("The area of the circle is:", result)