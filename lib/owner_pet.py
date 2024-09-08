class Pet:
    all=[]
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        self.pet_type=self.pet(pet_type)
        self.name=name
        self._owner=owner
        self.all.append(self)
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,value):
        if not isinstance(value,Owner):
             raise Exception("Owner must be an instance of the Owner class.")
        self._owner = value
    
    @classmethod
    def pet(cls,pet_type):
        if pet_type in cls.PET_TYPES:
            return pet_type
        else:
             raise ValueError(f"{pet_type} is not a valid pet type. Must be one of {cls.PET_TYPES}")
        

class Owner:
    def __init__(self,name):
        self.name=name
    
    def pets(self):
        return[pet for pet in Pet.all if pet.owner==self]
    
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise Exception("Pet must be an instance of pet class")
        pet.owner=self
    
    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet:pet.name)
    
miles=Pet("miles miley","dog",)
dave=Owner("dave")
dave.add_pet(miles)
