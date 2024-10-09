from math import pi


def square_side():
    try:
        return int(input("Please enter the squere side: "))
    except:
        return square_side()


def circle_radius():
    try:
        return int(input("Please enter the radius of the circle: "))
    except:
        return circle_radius()


def square_area(side):
    return side * side


def circle_area(radius):
    return pi * radius ** 2


square_area = square_area(square_side())
circle_area = circle_area(circle_radius())

print("Square area:", square_area)
print("Circle area:", circle_area)

if square_area > circle_area:
    print("The square area is larger")
elif square_area < circle_area:
    print("The circle area is larger")
else:
    print("Equal area")
