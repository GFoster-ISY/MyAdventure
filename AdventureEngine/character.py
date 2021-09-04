from map import Dirn
from utility import clear

class Character:
  def __init__(self, startx, starty):
    self.x = startx
    self.y = starty
    self.figure = "C"
    self.inRoom = True
    self.health = 100
    self.energy = 1000
    self.map = []
    self.error = ""
    self.level = ""

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
      print (f"Health: {self.health}  Energy: {self.energy} You are in the {roomName}")
    else:
      print (f"Health: {self.health}  Energy: {self.energy}")
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
