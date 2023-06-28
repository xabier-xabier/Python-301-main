# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

from random import randint

class Funcion_:

    def add_numbers():      # Create a list with 10 random numbers between 1-6
        list_=[]
        for i in range(1,11,1):
            x=randint(1,6)
            list_.append(x)
            count=10
        return list_
    
    def delete_num(num,lista):    # Delete 1 number in a list of ten whenever called this function
        lista.pop(num)
        return lista
    

if __name__=="__main__":
    print(len(Funcion_.add_numbers()))

    list_1=Funcion_.add_numbers()
    print(len(list_1))
    print(list_1)

    text=int(input("Please write a number between 1-10: "))

    new_list=Funcion_.delete_num(text,list_1)

    print(new_list)

