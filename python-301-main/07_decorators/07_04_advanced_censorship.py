# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor(func):
    def censor_text(text,censor1,censor2):
        if censor1 in text:
            long=len(censor1)
            new=text.replace(censor1,censor1[0]+"*"*(long-1))  # add the length of censor1 and censor2
        else:
            new=text
        if censor2 in new:
            long=len(censor2)
            new1=new.replace(censor2,censor2[0]+"*"*(long-1))
        else:
            new1=new
        return new1
    return censor_text

@censor
def say_something(text):
    return text

censor1=input("please write the word you want to censor: ")
censor2=input("please write the word you want to censor: ")
print(say_something("I want to go the beach on sunday morning",censor1,censor2))  