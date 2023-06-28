# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


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

def create_100_string(txt):
    war_100=list(txt)
    war_1=war_100[0:100]
    string_100=""
    for i in war_1:
        string_100+=i

    return string_100

class PrinceExecption(Exception):
    # Raised when "Prince" is included in the first 100 characters of the book
    pass


#Read war and peace txt file and store it in a variable
path="/Users/sagar/OneDrive/Escritorio/coding nomads/python-301-main/05_exceptions/books"
war_peace_txt=read_file(path,"war_and_peace.txt")       #It`s a string


crime_punish_txt=read_file(path,"crime_and_punishment.txt")
pride_prej_txt=read_file(path,"pride_and_prejudice.txt")

war_100=create_100_string(war_peace_txt)
crime_100=create_100_string(crime_punish_txt)
pride_100=create_100_string(pride_prej_txt)


try:
    war_100=create_100_string(war_peace_txt)

    if  "Prince" in war_100:
        raise PrinceExecption
    else:
        print("'Prince' is not included in the first 100 characters of war_and_peace.txt")
    
except PrinceExecption:
    print("'Prince' is included in the first 100 characters of war_and_peace.txt")

try:
    crime_100=create_100_string(crime_punish_txt)

    if  "Prince" in crime_100:
        raise PrinceExecption
    else:
        print("'Prince' is not included in the first 100 characters of crime_and_punishment.txt")
    
except PrinceExecption:
    print("'Prince' is included in the first 100 characters of crime_and_punishment.txt")


try:
    pride_100=create_100_string(pride_prej_txt)

    if  "Prince" in pride_100:
        raise PrinceExecption
    else:
        print("'Prince' is not included in the first 100 characters of pride_and_prejuice.txt")
    
except PrinceExecption:
    print("'Prince' is included in the first 100 characters of pride_and_prejuice.txt")