# Python lesson : type errors , type checking  
# and type conversion
# These three concepts are important when learning\
# python , reason is for they help you 
# understand how python handles different types
# of data
# 
# Lets go through  them  with examples you can
# type into Vs code
# 
# Type errors in python
# a typeerror happens when you try to perform
# an operation on a data type that python 
# can't handle in a particular way. 
# 
# Example :
# adding a string and an integer
age = 25
name = "Donny"

print(age + name)
# this will produce an error when you run it
# TypeError : unsupported operand type(s)
# for + "int " and "str"

# age is an integer (int)
# name is a string (str)
# Python can't directly add an integer and 
# a string
# How to fix it =
age = 25
name = "John"

print(str(age) + name)
