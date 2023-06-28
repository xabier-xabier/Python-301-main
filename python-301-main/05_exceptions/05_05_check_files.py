# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.
from pathlib import Path

def read_file(path,file_name):
    data_path=Path(path)
    with open(data_path.joinpath(file_name), "r") as file_in:
        numbers=file_in.read()
    return numbers


try:
    file_name = "integers.txt"
    path="/Users/sagar/OneDrive/Escritorio"
    numbers=read_file("/Users/sagar/OneDrive/Escritorio","integers.txt")
    num=numbers.split()
    val=int(num[0])
    
except IOError:
    print("I am sorry we couldn`t find the file in this path....")

except ValueError:
    print("Sorry but this file doesn`t contain integer number at least in first position")

else:
    print(val**2)
