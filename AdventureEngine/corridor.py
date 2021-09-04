class Corridor:
  def __init__(self, joins):
    self.joins = joins
    self.valdateJoins()
  
  def valdateJoins(self):
    i = 1
    while i < len(self.joins):
      start = self.joins[i-1]
      end = self.joins[i]
      if (start[0] != end[0] and start[1]!=end[1]):
        print(f"start {start} end {end} is invalid")
        return False
      i+=1
    return True

    
  def addToMap(self,level,locx=-1,locy=-1):
    i = 1
    while i < len(self.joins):
      start = self.joins[i-1]
      end = self.joins[i]
      if (start[0] == end[0]):
        if (start[1]< end[1]):
          if (locx == -1 or (locx==start[0] and locy>=start[1] and locy <= end[1])):
            for x in range(start[1],end[1]+1):
                level.placeOnMap(self,start[0],x,"█")
        else:
          if (locx == -1 or (locx==start[0] and locy>=end[1] and locy <= start[1])):
            for x in range(end[1],start[1]+1):
              level.placeOnMap(self,start[0],x,"█")
      elif (start[1] == end[1]):
        if (start[0]<end[0]):
          if (locx == -1 or (locy==start[1] and locx >= start[0] and locx<= end[0])):
            for x in range(start[0],end[0]+1):
              level.placeOnMap(self,x,start[1],"█")
        else:
          if (locx == -1 or (locy==start[1] and locx >= end[0] and locx<= start[0])):
            for x in range(end[0],start[0]+1):
              level.placeOnMap(self,x,start[1],"█")
      i+=1
