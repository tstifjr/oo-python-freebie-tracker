from .freebie import Freebie

class Dev:
    def __init__(self, name) :
        self.name = name
    

    @property
    def freebies(self):
        return [freebies for freebies in Freebie.all if self == freebies.dev]
    
    @property
    def companies(self):
        return [freebies.company for freebies in Freebie.all]
    
    def received_one(self, item_name) :
        for freebie in self.freebies :
          if item_name == freebie.item_name:
              return True
          
        return False
    
    def give_away(self, dev_ins, freebie_ins):
        for freebies in self.freebies:
            if freebies == freebie_ins:
                freebies.dev = dev_ins
                return f"given away a freebie to {dev_ins}"
        
        return f"{freebie_ins} is not owned"
            
        