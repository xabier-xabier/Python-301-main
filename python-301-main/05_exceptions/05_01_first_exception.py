# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

list_=["Hello world"]


try:
    print(list_[1])
except IndexError:
    print("sorry that option is not possible")

