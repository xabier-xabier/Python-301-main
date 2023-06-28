# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def wrap(func):
    def wrapper(text):
        return f'"{text}"'
    return wrapper

@wrap
def say_something(text):
    return text

print(say_something("Hello World"))  