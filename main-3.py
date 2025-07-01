# Python F-strings: Explained in detail with examples 
# # get familar with f-string syntax let writ a
# simple  program to display the temperature
# assigned to F temp
# first assign f to beginning of the string

# f_temp = 67

#  place a f before the sting in qutoes

# f"The temperature is 67 degrees Fahrenheit "

# next we need to take the 67 place in braces
# so we can convert regular string into a
# f string using the value of f_temp in the
# string writing the variable between the curtly
# braces not the literal string f_temp

# f"The temperature is {f_temp} degrees Fahrenheit"

# running the cell , we can see that the f_temp
# variable inside th f string was indeed replace
# by its value 67
#
# f string allows us to do much more , we can
# display the results of any expression between
# the braces  for example
#
# suppose we want our program to report the
# temperture in celcius instead of fahrenheit
#
# we can do the converison from fahrenheit
# directly inside  the f string by subtract 32
# from f_temp and dividing by 1.8  .When this line
# is executed , Python  first evaluates the
# conversion expression and then inserts the
#  results in the string if you run the results
# out willl out put many  19.44444444444 so to limit
# the output  numbers  so we want to limit the
# decimal  number which is easy.
#
# round numbers with f-string
# anytime we want to format the expression between
# brackets , we start by with a colon : and then  a
# period . , then we use 1f  to display the result
# as a float , if we wnat to display 2 digits  we
# 1.8:.2f for 2 digits display

f_temp = 67
print(f"The temperature is {(f_temp - 32) / 1.8:.2f} outside")
t_temp = 55
print(f"The current temperature  is {(t_temp - 32) / 1.8:.2f}")
