# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?


from pathlib import Path

def read_file(path,file_name):
    data_path=Path(path)
    with open(data_path.joinpath(file_name), "r",encoding="utf-8") as file_in:
        text=file_in.read()
    return text

def write_file(path,new_str):
    data_path=Path(path)
    with open(data_path.joinpath("crime_and_punishment.txt"), "w",encoding="utf-8") as file:
        file.write(new_str)


#Read war and peace txt file and store it in a variable
path="/Users/sagar/OneDrive/Escritorio/coding nomads/python-301-main/05_exceptions/books"
war_peace_txt=read_file(path,"war_and_peace.txt")       #It`s a string


# Re-write crime and punishment file with an empty string
crime_punish_txt=""                         #It`s an empty string Indexerror expected when calling "crime_punish_txt[0]`"
write_file(path,crime_punish_txt)

try:
    print(war_peace_txt[0])
    print(read_file(path,"pride_and_prejudice.txt")[0])  #Directly open the file and print first character
    print(crime_punish_txt[0])

except IndexError:
    print("The string it`s empty in crime_punish_txt variable")

