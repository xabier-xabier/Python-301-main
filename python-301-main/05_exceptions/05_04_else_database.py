# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

try:
    num1=float(input("please write the first number: "))
    num2=float(input("Please write the second number: "))
    print(num1/num2)
except ValueError:
    print("sorry write 2 numbers please")

except ZeroDivisionError:
    print("A number can`t be divided by zero")

else:
    print("good choice, the numbers are not words and it`s not divided by zero")
