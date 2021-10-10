from enum import Enum, auto
from utility import clear

class Dirn(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def newCoord(dirn, x,y):
      if dirn == Dirn.NORTH:
        return (x,y-1)
      if dirn == Dirn.EAST:
        return (x+1,y)
      if dirn == Dirn.SOUTH:
        return (x,y+1)
      if dirn == Dirn.WEST:
        return (x-1,y)

class Map:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.error = ""
    self.map = []
    self.lookup = []
    for i in range(width):
      self.map.append([" "] * height)
      self.lookup.append([""]* height)


  def placeOnMap(self,object, x,y,char):
    self.map[x][y] = char
    self.lookup[x][y] = object

  def getPlace(self):
    return self.lookup[self.character.x][self.character.y]

  def getNeighbour(self, x, y):
    try:
      return self.lookup[x][y]
    except:
      return ""

  def draw(self):
    clear()
    for y in range(self.height):
      for x in range(self.width):
        if (hasattr(self,'character') and self.character.x == x and self.character.y == y):
          print(self.character.figure, end="")
        else:
          print(self.map[x][y], end="")
      print()
    print(self.error)
    self.error = ""
  
  def moveTo(self, dirn, x, y):
    if dirn == Dirn.NORTH:
      if y-1 < 0:
        return ""
      return self.map[x][y-1]
    if dirn == Dirn.EAST:
      if x+1 >= self.width:
        return ""
      return self.map[x+1][y]
    if dirn == Dirn.SOUTH:
      if y+1 >= self.height:
        return ""
      return self.map[x][y+1]
    if dirn == Dirn.WEST:
      if x-1 < 0:
        return ""
      return self.map[x-1][y]

  def openDoor(self):
    x = self.character.x
    y = self.character.y
    for d in Dirn:
      (newx,newy) = Dirn.newCoord(d,x, y)
      if self.map[newx][newy] == "*":
        self.map[newx][newy] = "▒"
        self.character.map[newx][newy] = "▒"
        (farx,fary) =  Dirn.newCoord(d,newx, newy)
        where = self.lookup[newx][newy]
        where.openDoor(newx,newy)
        where.addToMap(self.character,farx,fary)
