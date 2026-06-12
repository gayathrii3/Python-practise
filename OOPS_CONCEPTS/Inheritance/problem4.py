class Skincare:  #base class
    consistency = "Gel-based"

    @staticmethod
    def started():
        print("clearing darkspots...")

    @staticmethod
    def stopped():
        print("skin purging...")

class summer(Skincare):       #child class

    def __init__(self, item, skintype):
        self.item = item
        self.skintype = skintype
        
class winter(summer):         #grandchild class  (multilevel inheritance)
    def __init__(self,item, skintype):
        super().__init__(item, skintype)
        
item1 = summer("moisturizer", "oily")
type1 = winter("Sunscreen", "Dry")


print(item1.item)
super().stopped()
# print(type1.skintype)
# print(type1.consistency)
# print(item1.stopped())