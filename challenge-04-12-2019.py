#!/usr/bin/env python3

debug = 1
if debug:
  import time
  start = time.perf_counter()

puzzle_input = range(372304, 847060)

def part1(input):
  matches = []
  
  for x in input:
    double = False
    increases = True
    xlist = list(str(x))
    for i in range(1, len(xlist)):
      if (xlist[i] == xlist[i - 1]):
        double = True
      if (int(xlist[i]) < int(xlist[i - 1])):
        increases = False
    if (double and increases):
      matches.append(x)
  
  return(matches)

def part2(passwds):
  
  nmatches = []
  
  for x in passwds:
    double = False
    xlist = list(str(x))
    for i in range(1, len(xlist)):
      if (xlist[i] == xlist[i - 1]):
        if (i + 1 < len(xlist) and i - 2 >= 0):
          if (xlist[i] != xlist[i + 1] and xlist[i] != xlist[i - 2]):
            double = True
        elif (i + 1 == len(xlist)):
          if (xlist[i] != xlist[i - 2]):
            double = True
        elif (i == 1):
          if (xlist[i] != xlist[i + 1]):
            double = True
    if (double):
      nmatches.append(x)
    
  return(len(nmatches))

amatches = part1(puzzle_input)
print("PartI:", len(amatches))
print("PartII:", part2(amatches))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
