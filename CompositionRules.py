from vessels import *

class Fleet:
    def __init__(self, name, faction, point_limit):
        self.name = name
        self.faction = faction
        self.point_limit = point_limit
        self.point_total = 0
        self.units = []
        self.fighter_limit = 0
        self.fighter_count = 0
        self.limited_limit = point_limit * .33
        self.restricted_limit = point_limit * .1
        self.limited_total = 0
        self.restricted_total = 0
       

    def add_unit(self, unit):
        if unit != Fighter:
            self.fighter_limit += unit.hanger_size
        else:
            self.fighter_count += 1
        self.units.append(unit)
        self.point_total += unit.cost
        if unit.rarity == "limited":
            self.limited_total += unit.cost
        if unit.rarity == "restricted":
            self.restricted_total += unit.cost
        self.validate_list()

    
    def remove_unit(self, unit):
        if unit != Fighter:
            self.fighter_limit -= unit.hanger_size
        else:
            self.fighter_count -= 1
        self.units.remove(unit)
        self.point_total -= unit.cost
        if unit.rarity == "limited":
            self.limited_total -= unit.cost
        if unit.rarity == "restricted":
            self.restricted_total -= unit.cost
        self.validate_list()

    
    def validate_list(self):
        if self.point_total > self.point_limit:
            raise Exception("Point total over limit")
        if self.fighter_count > self.fighter_limit:
            raise Exception("Not enough hanger space for fighters")
        if self.restricted_total > self.restricted_limit:
            raise Exception("Restricted total over restricted limit")
        if self.limited_total > self.limited_limit:
            raise Exception("Limited total over limit")
        else: 
            print(self.units)
            print(f"{self.point_total} / {self.point_limit}")
        

