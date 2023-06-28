# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

integer=False
while integer==False:

    try:
        num1=int(input("Please write a integer: "))
        integer=True
    except TypeError:
        print("that type is not valid")
    except ValueError:
        print("That`s not a integer")
 






