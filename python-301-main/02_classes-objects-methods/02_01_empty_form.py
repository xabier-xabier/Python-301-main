# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Doctor_office():

    def __init__(self,name,surname,birth_date,disease,treatment):
        self.name=name
        self.surname=surname
        self.birth_date=birth_date
        self.disease=disease
        self.treatment=treatment
        pass

    def __str__(self) -> str:
        return f"""
            The patient {self.name}, {self.surname}, 
            birth date {self.birth_date} suffers of {self.disease}
            and is under {self.treatment} treatment"""
        pass


name=input("please write your name: ")
sur=input("Please write your surname: ")
birth=input("please write your birth date: ")
disease=input("write if you have any disease: ")
treatment=input("write if you are under any treatment: ")

nombre=Doctor_office(name,sur,birth,disease,treatment)
print(nombre)
print(nombre.name, nombre.surname)
print(nombre.disease)
print(nombre.birth_date)
