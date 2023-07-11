from .freebie import Freebie

class Company:
    all = []
    def __init__(self, name, year) :
        self.name = name
        self.year = year
        Company.all.append(self)
    @property
    def freebies (self):
        return [freebies for freebies in Freebie.all if self == freebies.company]
    
    @property
    def devs (self):
        return [freebies.dev for freebies in self.freebies]
    
    def give_freebie(self, dev_instance, item_name, value):
        Freebie(dev_instance, self, item_name, value)

    @classmethod
    def oldest_company(self):
        old_year = 0
        for company in Company.all:
            if old_year == 0 :
                old_year = company.year
            else:
                if old_year > company.year:
                    old_year = company.year

        return old_year
       
        # my_sort = sorted(Company.all, key = lambda c : c.year)
        # if len(my_sort) > 0:
        #     return my_sort[0]
        # else :
        #     raise Exception("there are no companies")