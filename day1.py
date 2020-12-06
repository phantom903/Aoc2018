from itertools import cycle

class DayOne:

  freqList = []
  
  def __init__(self, mem):
    self.freqList = mem.copy()
  
  def partOne(self):
    return sum(self.freqList)

  def partTwo(self):
    freqs = {0}
    curFreq = 0
    for freq in cycle(self.freqList):
      curFreq += freq
      if curFreq in freqs:
        return curFreq
      else:
        freqs.add(curFreq)
    

