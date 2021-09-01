# from arithmetic.arith import Coords # If we wouldn't have written the import statement in the arithmetic package __init__.py file
from arithmetic import Coords   # This is direct import of the Coords class because we have imported the Coords in the package __iit__.py file
# Remember, if the package is not installed in the environment, then the relative path must be present to locate jus the package.
# In addition, if__init__.py of the package is not prsent, then also the whole complete path to the entity should be written


import random
from functools import reduce


# In case to print the location of the package location (present for the current environment) on the system:
# This will only work if the package is installed in the environment. Else complete path will be asked to locate the package, which is absurd!
print('Package Location is : ', arithmetic.__file__)
print('\n'*2)

""" https://docs.python.org/3/library/random.html """
x = [random.randint(1, 10) for itr in range(10)]
y = [random.randint(1, 10) for itr in range(10)]
print(x)
print(y)
coords_list = [Coords(*points) for points in zip(x, y)]


print('First Coord : ', coords_list[0])

# Test of object +- numeral
print('*'*10)
print(coords_list[0] + 5)
print('*'*10)
print(coords_list[0] - 5)

# Test of numeral +- object (test of __radd__ and __rsub__)
print('*'*10)
print(5.0 + coords_list[0])
print('*'*10)
print(5.0 - coords_list[0])

# Test of object + string(exception case) ONLY FOR ADDITION
print('*'*10)
print(coords_list[0] + 'sharan')
# Test of string(exception case) + object ONLY FOR ADDITION
print('*'*10)
print('sharan' + coords_list[0])

# Test of object - string(exception case) ONLY FOR SUBTRACTION
print('*'*10)
print(coords_list[0] - 'sharan')
# Test of string(exception case) - object ONLY FOR SUBTRACTION
print('*'*10)
print('sharan' - coords_list[0])

print('*'*20)
print(Coords(10,4)+Coords(5,9))

print('*'*10)
# Test of object +- object
add = reduce((lambda x, y : x+y), coords_list)
# print(type(add), add.abscissa, add.ordinate)
print('Addition : ', add)
sub = reduce((lambda x, y : x-y), coords_list)
# print(type(sub), sub.abscissa, sub.ordinate)
print('Subtraction : ', sub)

# print('*'*20)
# coords_list[0].experiment()