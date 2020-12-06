from aoc import *

class DayTwo:

  packIds = []

  def __init__(self, mem):
    self.packIds = mem.copy()

  def partOne(self):
    totalTwos = []
    totalThrees = []
    for line in self.packIds:
      two = False
      three = False
      letters = set(line)
      for i in letters:
        count = line.count(i)
        if count == 2:
          two = True
        if count == 3:
          three = True
      totalTwos.append(two)
      totalThrees.append(three)
    return sum(totalThrees) * sum(totalTwos)