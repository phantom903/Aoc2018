from aoc import *

def splitClaim(claim):
  result = []
  claim = claim.split(' ')
  result.append(claim[2].split(',')[0])
  result.append(claim[3].split('x')[0])
  result.append(claim[2].split(',')[1].strip(':'))
  result.append(claim[3].split('x')[1])
  print(result)

class DayThree:

  claims = []

  def __init__(self, mem):
    self.claims = mem.copy()

  def partOne(self):
    for i in self.claims:
      claim = splitClaim(i)
      

  def partTwo(self):
    pass