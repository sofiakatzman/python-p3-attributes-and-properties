#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    #initialization of properties along with default values to prevent error 
    def __init__(self, name='Sofia', breed='Pointer'):
        self.name = name
        self.breed = breed

    #get method for name  
    def get_name(self): 
        return self._name

    #set method for name
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    
    #property constructor method for name 
    name = property(get_name, set_name)        


    #get method for breed
    def get_breed(self): 
        return self._breed


    #set method for breed
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS: 
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")    


    #property constructor method for breed
    breed = property(get_breed, set_breed)