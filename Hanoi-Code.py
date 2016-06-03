"""
This program allows the user play the game "The Towers of Hanoi", giving them the option of selecting the number of disks they would like to begin with. 

Omodayo Origunwa
Spring 2016
"""


def getInt(s,low,high):
  while True:
    n = raw_input(s)
    try:
      n = int(n)
      if (1 <= n <= 9):
        return n
      else:
        print("Please enter an integer between 1 and 9 ")
        True
    except ValueError:
      print("Please enter an integer between 1 and 9 ")


def diskMoveable(disk,rod1,rod2,rod3):
  d = disk
  if (len(rod1) == 0):       #if rod has no length, do nothing
    m = "taco"
  elif (d == rod1[-1]):     #if rod has length and disk = top value, output true and leave loop
    m = True
    return m
  else:                     #otherwise, continue searching 
    m = False

  if (len(rod2) == 0):
    m = "taco"
  elif (d == rod2[-1]):
    m = True
    return m
  else:
    m = False

  if (len(rod3) == 0):
    m = "taco"
  elif (d == rod3[-1]):
    m = True
    return m
  else:
    m = False


def getValidMove(ndisks,rod1,rod2,rod3):
  i = 0
  while i == 0:
    disk = raw_input("Which disk would you like to move? ")
    try:                                    #verify that input is valid 
      disk = int(disk)
      if (1 <= disk <= ndisks):
        m = diskMoveable(disk,rod1,rod2,rod3)  #check to see if disk is @ the top of a rod. If it is, break. Else, continue loop
        if m == True:
          return disk  #send valid disk to main
        else:
          print("You cannot move that disk. Please choose one at the top of a rod ")
          print(rod1)
          print(rod2)
          print(rod3)
      else:
        print("Please enter an integer between 1 and %d " %(ndisks))
    except ValueError:
      print("Please enter an integer between 1 and %d " %(ndisks))



def checkRod(disk,rod):
  d = disk
  if (len(rod) == 0):      #Check to see if rod is empty
    return True
  elif (d > rod[-1]):
    print("That is an invalid move! Disks must be stacked in descending order!")
    return False
  else:
    return True



def getValidRod(disk,rod1,rod2,rod3):
  d = disk
  while True:
    mov_rod = raw_input("Which rod would you like to move disk %d to? " %(disk))
    try:
      mov_rod = int(mov_rod)
      if (1 <= mov_rod <= 3):
        if (mov_rod == 1):
          k = checkRod(disk,rod1)
        elif (mov_rod == 2):
          k = checkRod(disk,rod2)
        elif (mov_rod == 3):
          k = checkRod(disk,rod3)
        if (k != False):
          return mov_rod            #outputs k which is mov_rod which is the initial rod of the disk in question @ this poin 
      else:
        print("Please enter an integer between 1 and 3 ")
    except ValueError:
      print("Please enter an integer between 1 and 3 ")


def move(disk,mov_rod,rod1,rod2,rod3):
  d = disk
  if (len(rod1) != 0) and (disk == rod1[-1]):
    j = rod1
  elif (len(rod2) != 0) and (disk == rod2[-1]):
    j = rod2
  elif (len(rod3) != 0) and (disk == rod3[-1]):
    j = rod3
  p =  j.pop()
  if (mov_rod == 1):
    mov_rod = rod1
  elif (mov_rod == 2):
    mov_rod = rod2
  elif (mov_rod == 3):
    mov_rod = rod3
  mov_rod.append(p)


def printState(rod1,rod2,rod3):
  print("Rod 1: %s" % (rod1))
  print("Rod 2: %s" % (rod2))
  print("Rod 3: %s" % (rod3))

def isGameOver(rod1,rod2,rod3):
  if (len(rod1) == 0 and len(rod2) == 0):
    return True
  else:
    return False

def main():
    s = "How many disks do you want? "
    low = 1
    high = 9
    ndisks = getInt(s,low,high)
    rod1 = range(ndisks,0,-1)
    rod2 = []
    rod3 = []
    while not isGameOver(rod1,rod2,rod3):
      printState(rod1,rod2,rod3)
      disk = getValidMove(ndisks,rod1,rod2,rod3)
      g = getValidRod(disk,rod1,rod2,rod3)
      move(disk,g,rod1,rod2,rod3)
    print("Congratulations!! You Won!")

main()

def test():

  #instantiate variables 
  s = "How many disks do you want? "
  low = 1
  high = 9
  i = 0
  rod = 0


  #call functions
  ndisks = getInt(s,low,high)
  rod1 = range(ndisks,0,-1)
  rod2 = []
  rod3 = []
  disk = getValidMove(ndisks,rod1,rod2,rod3)
  g = getValidRod(disk,rod1,rod2,rod3)
  c = move(disk,g,rod1,rod2,rod3)
  printState(rod1,rod2,rod3)
  #test()
