# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


def wrap(func):
    def wrapper(text):
        if "Shoot" in text:
            new=text.replace("Shoot","S****")
        else:
            new=text
        if "shoot" in new:
            new1=new.replace("shoot","s****")
        else:
            new1=new
        return new1
    return wrapper

@wrap
def say_something(text):
    return text

print(say_something("Don`t shoot please, shoot to other one. Shoot him"))  