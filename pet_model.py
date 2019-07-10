'''
Created on Jul 10, 2019

@author: underit
'''


class Pets(object):
    """
    This class will represent a class for pets
    """

    def __init__(self, name, owner):
        """
        creates the variables associated with the class
        
        :type name: string
        :param name: the name of the pet
        
        :type owner: string
        :param owner: the name of owner
        """
        self.name = []
        self.owner = owner
        self.name.append(name)
    
    def add_pet(self, name):
        """
        adds a pet to the pet list
        
        :type name: string
        :param name : pet name to add to list of pets
        """
        
        self.name.append(name)

    def show_pets(self):
        """
        print out all the pets from the list
        """
        print("The owner of these pets :  " + self.owner)
        for each in self.name:
            print(each)
