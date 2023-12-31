#!/usr/bin/python3
# Rectangle = __import__('0-rectangle').Rectangle

# my_rectangle = Rectangle()
# print(type(my_rectangle))
# print(my_rectangle.__dict__)

# my_rectangle = Rectangle(2, 4)
# print(my_rectangle.__dict__)

# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle.__dict__)

# Rectangle = __import__('3-rectangle').Rectangle

# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# print(str(my_rectangle))
# print(repr(my_rectangle))

# print("--")

# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle)
# print(repr(my_rectangle))

#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

