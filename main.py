import sys
sys.path.insert(1, 'AdventureEngine')
from utility import getch
from character import Character
from room import Room
from item import Food, FirstAid, Chest, Key
from corridor import Corridor
from map import Map, Dirn

r1 = Room("Bedroom", 10,8,50,17)
r1.addDoor(Dirn.NORTH, 1)
r1.addDoor(Dirn.EAST, 2)
 
r2 = Room("Kitchen", 23, 12,12,2)
r2.addDoor(Dirn.SOUTH, 2)
r2.addDoor(Dirn.EAST,1)
 
r3 = Room("Hallway", 12, 15,0,8)
r3.addDoor(Dirn.NORTH, 1)
r3.addDoor(Dirn.EAST,1)
 
level = Map(66,25)
 
r1.addToMap(level)
r2.addToMap(level)
r3.addToMap(level)

c1 = Corridor([ [35,8], [55,8], [55,16] ])
c1.addToMap(level)
c2 = Corridor([ [60,19], [65,19], [65,22], [60,22] ])
c2.addToMap(level)
c3 = Corridor([ [6,7], [6,1], [48,1], [48,7] ])
c3.addToMap(level)
c4 = Corridor([ [12,15], [16,15], [16,24], [1,24] ])
c4.addToMap(level)
c5 = Corridor([ [19,14], [19,17], [27,17], [27,14] ])
c5.addToMap(level)

item1 = Food(3,5,19)
item1.addToMap(level)
item2 = Chest(1,4,19)
item2.addToMap(level)
item3 = Key(1,2,18)
item3.addToMap(level)
item4 = Key(1,2,15,item2)
item4.addToMap(level)

player = Character(2,21,startEnergy=500)
player.addToMap(level)
player.draw()
#player.addToInventory(Food(5))
#player.addToInventory("Gold",25)
player.addToInventory(FirstAid(1))

# player.listInventory()
# player.removeFromInventory("Food",5)
# player.listInventory()
# player.addToInventory("Food",5)
# player.listInventory()

# level.draw()

while True:
  command = getch()
  command = command[0].upper()
  if command == "N":
    player.move(Dirn.NORTH)
  if command == "E":
    player.move(Dirn.EAST)
  if command == "S":
    player.move(Dirn.SOUTH)
  if command == "W":
    player.move(Dirn.WEST)
  if command == "O":
    level.openDoor()
  if command == "P":
    player.pickupItem()
  if command == "U":
    player.useItem()
  if command == "I":
    player.listInventory()

  if player.energy == 0:
    print ("You died of exhaustion")
    break
  if player.health == 0:
    print ("You died of bloodloss")
    break
  if player.finished:
    print ("Congratulations you win.")
    break

  player.draw()
