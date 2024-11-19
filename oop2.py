#create a class called r person,that has three attributes,name,age and gender
#then create a constructor method and object
from tkinter.font import names

from oop import myobj


class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print("my name is {self.name} iam {self.age} years old {self.gender}")

myobj=person