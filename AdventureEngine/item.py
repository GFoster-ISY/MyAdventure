from abc import abstractmethod

class Item:
  def __init__(self, amount, startx=-1, starty=-1, portable=True):
    self.name = "Thing"
    self.amount = amount
    self.canCarry = portable
    self.x = startx
    self.y = starty
    self.figure = "#"
    
  def __str__(self):
    if self.amount == 1:
      return f"a {self.name}"
    else:
      return f"{self.amount} {self.name}"
  
  def addToMap(self, map):
    where = map.getLocation(self.x, self.y)
    where.addItem(map, self)

  @abstractmethod
  def use(self, map, player):
    pass
  
  # def drop(self, map, player):
  #   player.removeFromInventory(self.name, self.amount)
  #   self.addToMap(map)

class Food(Item):
  def __init__(self, amount, startx=-1, starty=-1, portable=True):
    Item.__init__(self, amount, startx, starty, portable)
    self.name = "Food"
    self.figure = "F";

  def use(self, map, player):
    player.addToEnergy(100)

class FirstAid(Item):
  def __init__(self, amount, startx=-1, starty=-1, portable=True):
    Item.__init__(self, amount, startx, starty, portable)
    self.name = "First Aid Kit"
    self.figure = "+";
    
  def use(self, map, player):
    player.addToHealth(50)