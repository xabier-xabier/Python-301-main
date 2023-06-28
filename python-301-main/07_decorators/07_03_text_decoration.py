# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


def decorator(func):
    def text_decorator(text,arg):
        return f"""
        {arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}
        {text}
        {arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}{arg}"""
    return text_decorator

@decorator
def say_something(text):
    return text

print(say_something("Hello World","*"))  