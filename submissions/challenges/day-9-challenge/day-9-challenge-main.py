print("=======================================")
print("|\tArea of Circle Calculator     |")
print("=======================================")
radius = int(input("Enter the value of the radius: "))

from calculate_area import CircleArea
area = CircleArea(radius)

print(f"Area of Circle: {area}\n")