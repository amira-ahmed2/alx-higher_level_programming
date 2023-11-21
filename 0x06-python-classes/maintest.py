#!/usr/bin/python3
# task0
# Square = __import__('0-square').Square

# my_square = Square()
# print(type(my_square))
# print(my_square.__dict__)

# task1
# Square = __import__('1-square').Square

# my_square = Square(3)
# print(type(my_square))
# print(my_square.__dict__)

# try:
#     print(my_square.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square.__size)
# except Exception as e:
#     print(e)

# task5
# Square = __import__('5-square').Square

# my_square = Square(3)
# my_square.my_print()

# print("--")

# my_square.size = 10
# my_square.my_print()

# print("--")

# my_square.size = 0
# my_square.my_print()

# print("--")

# task6

Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
