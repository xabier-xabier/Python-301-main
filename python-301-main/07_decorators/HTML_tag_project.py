
import time


def paragraph(func):
    def para_wrapper(text,tag):
        return f"<{tag}>{text}<{tag}>"
    return para_wrapper

def check_tag_exists(tag):
    lista=["p","head","title","body","a","h1","h2","h3","h4","h5","h6"]
    if tag in lista:
        result=True
    else:
        result=False
    return result

@paragraph
def say_something(text):
    return text


if __name__ == '__main__':
   tag=input("please write the type of tag you want to use: ")
   text=input("Please write the sentence you want to print: ")
   if check_tag_exists(tag)==True:
       print(say_something(text,tag))
   else:
       print(f"sorry but {tag} doesn`t exist in HTML tag")