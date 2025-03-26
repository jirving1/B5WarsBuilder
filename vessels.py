# contains ship and fighter classes
#initial use is 
class Ship:
  def  __init__(self, faction, name, ship_class, rarity, in_service, hanger_size, cost):
    self.faction = faction
    self.name = name
    self.ship_class = ship_class
    self.rarity = rarity 
    self.in_service = in_service
    self.hanger_size = hanger_size
    self.cost = cost
  
  def __repr__(self):
    return f"{self.faction} {self.name} | Rarity: {self.rarity} | In service: {self.in_service} | Hanger Size: {self.hanger_size} | Cost: {self.cost}"

class ShipVariant(Ship):
  def __init__(self, variant_of):
    super().__init__()
    self.variant_of = variant_of



class Fighter:
  def __init__(self, faction, name, ship_class, in_service, cost):
    self.faction = faction
    self.name = name
    self.ship_class = ship_class
    self.in_service = in_service
    self.cost = cost

  def __repr__(self):
    return f"{self.faction} {self.name} | In service: {self.in_service} | Cost: {self.cost}"


class Structure(Ship):
  def __init__(self):
    super().__init__()
    

