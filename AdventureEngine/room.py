# Useful website for the extended ASCII characters
# https://www.sciencebuddies.org/science-fair-projects/references/ascii-table#extendedasciitable

import math
from map import Dirn

class Room:
  def __init__(self, name, width, height, offsetx, offsety):
    self.name = name
    self.width = width
    self.height = height
    self.offsetx = offsetx
    self.offsety = offsety
    self.door = []
    self.doorOpen = []

  def __repr__(self):
    text = f"Object Room\n   Width : {self.width}\n   Height: {self.height}\n   Doors : {self.door}\n"
    return text

  def globalToLocal (self, gx, gy):
    return (gx-self.offsetx, gy-self.offsety)

  def localToGlobal (self, lx, ly):
    return (lx+self.offsetx, ly+self.offsety)


  def addDoor(self, side, count):
    if side == Dirn.NORTH:
      for x in range(count):
        posn = math.floor((x+1)*self.width/(count+1))
        self.door.append((posn,0))
    elif side == Dirn.EAST:
      for x in range(count):
        posn = math.floor((x+1)*self.height/(count+1))
        self.door.append((self.width-1,posn))
    elif side == Dirn.SOUTH:
      for x in range(count):
        posn = math.floor((x+1)*self.width/(count+1))
        self.door.append((posn,self.height-1))
    elif side == Dirn.WEST:
      for x in range(count):
        posn = math.floor((x+1)*self.height/(count+1))
        self.door.append((0,posn))
  
  def openDoor (self, gx, gy):
    (locx, locy) = self.globalToLocal(gx,gy)
    if (locx, locy) not in self.doorOpen:
      self.doorOpen.append((locx, locy))

  def addToMap(self,level,charGx=-1,charGy=-1):
    if (self.width + self.offsetx > len(level.map)):
      level.error = f"The room {self.name} will not fit into the map with a horizontal offset of {self.offsetx}"
      return
    if (self.height + self.offsety > len(level.map[0])):
      level.error = f"The room {self.name} will not fit into the map with a vertical offset of {self.offsety}"
      return
    (charLx, charLy) = self.globalToLocal(charGx, charGy)
    if (charGx == -1 or (charLx > 0 and charLx < self.width -1 and charLy > 0 and charLy < self.height -1)):
      for ly in range(self.height):
        for lx in range(self.width):
          (gx, gy) = self.localToGlobal(lx,ly)
          if ((lx,ly) in self.door):
            if ((lx,ly) in self.doorOpen):
              level.placeOnMap(self,gx,gy,"▒")
            else:
              level.placeOnMap(self,gx,gy,"*")
          elif ((lx == 0 and ly == 0) ):
            level.placeOnMap(self,gx,gy,"╔")
          elif (lx == self.width-1 and ly == 0):
            level.placeOnMap(self,gx,gy,"╗")
          elif (lx == 0 and ly == self.height-1):
            level.placeOnMap(self,gx,gy,"╚")
          elif (lx == self.width-1 and ly == self.height-1):
            level.placeOnMap(self,gx,gy,"╝")
          elif (lx==0 or lx==self.width-1):
            level.placeOnMap(self,gx,gy,"║")
          elif (ly==0 or ly==self.height-1):
            level.placeOnMap(self,gx,gy,"═")
          else:
            level.placeOnMap(self,gx,gy," ")
    elif ((charLx,charLy) in self.door):
      if ((charLx,charLy) in self.doorOpen):
        level.placeOnMap(self,charGx,charGy,"▒")
      else:
        level.placeOnMap(self,charGx,charGy,"*")

  