#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed= "Mutt" ):
        self.name = name
        self.breed = breed
        print(f"{name} is born!")

    def bark(self, name):
        self.name = name
        print("Woof!")
        print(f"{self.name} is barking!")

    def get_adopted(self, owner_name):
        self.owner = owner_name
        print(f"{self.name} has been adopted by {owner_name}!")

    # def showing_self(self):
    #     return self

    # pass

fido = Dog("Fido")
fido.name
fido.bark("Fido")
fido.get_adopted("Sophie")
fido.owner

# fido.showing_self()

snoopy = Dog("Snoopy")
snoopy.name