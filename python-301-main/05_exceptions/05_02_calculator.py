# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.


try:
    num1=float(input("please write the first number: "))
    num2=float(input("Please write the second number: "))
    print(num1/num2)
except ValueError:
    print("sorry write 2 numbers please")

except ZeroDivisionError:
    print("A number can`t be divided by zero")
