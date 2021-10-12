from map import Dirn
from utility import clear, getch

class Character:
  def __init__(self, startx, starty, startHealth=100, startMaxHealth=100, startEnergy=1000, startMaxEnergy=1000):
    self.x = startx
    self.y = starty
    self.figure = "C"
    self.inRoom = True
    self.maxHealth = startMaxHealth;
    self.maxEnergy = startMaxEnergy;
    self.setHealth(startHealth)
    self.setEnergy(startEnergy)
    self.map = []
    self.error = ""
    self.level = ""
    self.inventory = {}

  def setHealth(self, newHealth):
    if (newHealth > self.maxHealth):
      newHealth = self.maxHealth
    self.health = newHealth;

  def setEnergy(self, newEnergy):
    if (newEnergy > self.maxEnergy):
      newEnergy = self.maxEnergy
    self.energy = newEnergy
  
  def addToInventory(self,item, amount):
    if (item in self.inventory):
      self.inventory[item] += amount
    else:
      self.inventory[item] = amount

  def removeFromInventory(self, item, amount):
    if (item in self.inventory):
      if self.inventory[item] > amount:
        self.inventory[item] -= amount
      else:
        self.inventory.pop(item)

  def listInventory(self):
    clear()
    if self.inventory == {}:
      print("You are carrying nothing")
    else:
      print("You are carrying:")
      for item in self.inventory:
        print(f"{item}: {self.inventory[item]}")
    print("Press any key to continue")
    getch()

  def pickupItem(self):
    None

  def useItem(self):
    clear()
    print("Which item would you like to use?")
    index = 1
    for item in self.inventory:
      print(f"{index}: {item} -> {self.inventory[item]}")
      index += 1
    print("Select a number.")
    itemIndex = int(getch())
    if (itemIndex < index):
      item = list(self.inventory.keys())[itemIndex-1]
      print(f"You used {item}")
    self.removeFromInventory(item,1)
    print("Press any key to continue")
    getch()

  def addToMap(self, level):
    self.level = level
    level.character = self
    self.map = []
    for i in range(level.width):
      self.map.append([" "] * level.height)
    where = level.getPlace()
    where.addToMap(self)

  def draw(self):
    clear()
    if (self.inRoom):
      where = self.level.getPlace()
      roomName = where.name
      roomDetails = f" You are in the {roomName}"
    else:
      roomDetails = ""
    print (f"Health: {self.health}/{self.maxHealth}  Energy: {self.energy}/{self.maxEnergy} {roomDetails}")
    for y in range(len(self.map[0])):
      for x in range(len(self.map)):
        if (self.x == x and self.y == y):
          print(self.figure, end="")
        else:
          print(self.map[x][y], end="")
      print()
    print(self.error)
    self.error = ""

  def placeOnMap(self,object, x,y,char):
    self.map[x][y] = char

  def move(self, dirn):
    ahead = self.level.moveTo(dirn, self.x, self.y)
    if ahead == "":
      self.error = "You have reached the edge of the world"
    elif ahead == " " and self.inRoom:
      (self.x,self.y) = Dirn.newCoord(dirn,self.x, self.y)
    elif ahead == " " and not self.inRoom:
      self.error = "Ouch you hit a wall."
      self.health -= 2
    elif ahead == "║" or ahead == "═":
      self.error = "Ouch you hit a wall."
      self.health -= 1
    elif ahead == "*":
      self.error = "You need to open the door"
    elif ahead == "▒":
      (self.x,self.y) = Dirn.newCoord(dirn,self.x, self.y)
      self.inRoom = True;
    elif ahead == "█":
      (self.x,self.y) = Dirn.newCoord(dirn,self.x, self.y)
      where = self.level.getPlace()
      where.addToMap(self,self.x,self.y)
      for d in Dirn:
        (newx,newy) = Dirn.newCoord(d, self.x, self.y)
        where = self.level.getNeighbour(newx, newy)
        if where != "":
          where.addToMap(self, newx, newy)
      self.inRoom = False;
    self.energy -= 1
