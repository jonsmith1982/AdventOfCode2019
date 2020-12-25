#!/usr/bin/env python3

import re

debug = 1
if debug:
  import time
  start = time.perf_counter()

with open("challenge-03-12-2019.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):

  def move(d, a, x, y):
    moves = []
    if (d == 'R'):
      for i in range(1, a + 1):
        x += 1
        moves.append((x, y))
    elif (d == 'U'):
      for i in range(1, a + 1):
        y += 1
        moves.append((x, y))
    elif (d == 'L'):
      for i in range(1, a + 1):
        x -= 1
        moves.append((x, y))
    elif (d == 'D'):
      for i in range(1, a + 1):
        y -= 1
        moves.append((x, y))
    return(moves)
  
  lhistory = [(0, 0)]
  lwire = re.split(',', input[0])
  for x in lwire:
    d = x[0]
    a = int(x[1:])
    (x, y) = lhistory[-1]
    lhistory += move(d, a, x, y)
  
  rhistory = [(0, 0)]
  rwire = re.split(',', input[1])
  for x in rwire:
    d = x[0]
    a = int(x[1:])
    (x, y) = rhistory[-1]
    rhistory += move(d, a, x, y)
  
  ahistory = list(set(lhistory.copy()) & set(rhistory.copy()))
  
  closest = 0
  for x, y in ahistory:
    if (x == 0 and y == 0):
      continue
    if (x < 0):
      x = int(str(x)[1:])
    if (y < 0):
      y = int(str(y)[1:])
    val = x + y
    if (val < closest or closest == 0):
      closest = val
  
  return(closest)

def part2(input):

  def move(d, a, x, y):
    moves = []
    if (d == 'R'):
      for i in range(1, a + 1):
        x += 1
        moves.append((x, y))
    elif (d == 'U'):
      for i in range(1, a + 1):
        y += 1
        moves.append((x, y))
    elif (d == 'L'):
      for i in range(1, a + 1):
        x -= 1
        moves.append((x, y))
    elif (d == 'D'):
      for i in range(1, a + 1):
        y -= 1
        moves.append((x, y))
    return(moves)
  
  lhistory = [(0, 0)]
  lwire = re.split(',', input[0])
  for x in lwire:
    d = x[0]
    a = int(x[1:])
    (x, y) = lhistory[-1]
    lhistory += move(d, a, x, y)
  
  rhistory = [(0, 0)]
  rwire = re.split(',', input[1])
  for x in rwire:
    d = x[0]
    a = int(x[1:])
    (x, y) = rhistory[-1]
    rhistory += move(d, a, x, y)
  
  ahistory = list(set(lhistory.copy()) & set(rhistory.copy()))
  
  closest = 0
  for x, y in ahistory:
    if (x == 0 and y == 0):
      continue
    l_steps = lhistory.index((x, y))
    r_steps = rhistory.index((x, y))
    if (l_steps + r_steps < closest or closest == 0):
      closest = l_steps + r_steps
  
  return(closest)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
