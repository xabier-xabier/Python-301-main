# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

class Movie():

    def __init__(self,year,title):
        self.year=year
        self.title=title
        pass

    def __str__(self):
        return f""" the year of the movie is {self.year} and the title is {self.title}"""

class RomCom(Movie):
    pass

class ActionMovie(RomCom):

    def __init__(self, year, title,pg):
        super().__init__(year, title)
        pg=13
        self.pg=pg

    def __str__(self):
        return f"""
                the year of creation is {self.year} the title is {self.title}
                            the pg value is {self.pg}"""


r1=ActionMovie(2005,"Terminator",10)
print(r1)
print("\n")
r2=Movie(2005,"Terminator")
print(r2)