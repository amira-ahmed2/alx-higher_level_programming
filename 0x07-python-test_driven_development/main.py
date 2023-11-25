#!/usr/bin/python3

# add_integer = __import__('0-add_integer').add_integer

# print(add_integer(1, 2))
# print(add_integer(100, -2))
# print(add_integer(2))
# print(add_integer(100.3, -2))
# try:
#     print(add_integer(4, "School"))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer(None))
# except Exception as e:
#     print(e)

# task2
"""
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
"""
# task3

#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)