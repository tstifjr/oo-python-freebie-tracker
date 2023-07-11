
class Freebie:
    all = []
    def __init__(self, dev, company, item_name, value):
        self.dev = dev
        self.company = company
        self.item_name = item_name
        self.value = value
        Freebie.all.append(self)

    @property
    def company (self):
        return self._company
        
    @company.setter
    def company(self, new_company):
        from .company import Company
        if isinstance(new_company, Company):
            self._company = new_company
        else : raise Exception

    def print_details(self) :
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"