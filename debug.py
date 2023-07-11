import ipdb
from lib import *

#code here
c1 = Company("Htech", 2005)
c2 = Company("Iop", 2009)
c3 = Company("Almon", 1999)
c4 = Company ("QQQ", 2021)
d1 = Dev("Karl")
d2 = Dev("Ralph")
f1 = Freebie(d1, c1, "Mug", 5)
f2 = Freebie(d1, c2, "Towel", 20)

ipdb.set_trace()