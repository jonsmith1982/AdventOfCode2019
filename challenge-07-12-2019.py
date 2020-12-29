#!/usr/bin/env python3

import itertools

debug = 1
if (debug):
  import time
  start = time.perf_counter()

with open("challenge-07-12-2019.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  program_data = [int(x) for x in input[0].split(',')]

  def intcode(data, x, y):
    program_input = [x, y]
    program_output = []
    next_op = 0
    i = 0
    
    while (next_op != 99):
      ap, bp = 0, 0
      next_op = data[i]
      
      if (len(str(next_op)) >= 3):
        ap = int(str(next_op)[-3])
        if (len(str(next_op)) >= 4):
          bp = int(str(next_op)[-4])
        next_op = int(str(next_op)[-1])
      
      a = data[i + 1]
      if (ap == 0 and next_op != 3 and len(data) > a):
        a = data[a]
      if (len(data) > i + 2):
        b = data[i + 2]
        if (bp == 0 and len(data) > b):
          b = data[b]
      if (len(data) > i + 3):
        c = data[i + 3]
  
      if (next_op == 1):
        data[c] = a + b
        i += 4
      elif (next_op == 2):
        data[c] = a * b
        i += 4
      elif (next_op == 3):
        data[a] = program_input.pop(0)
        i += 2
      elif (next_op == 4):
        program_output.append(a)
        i += 2
      elif (next_op == 5):
        if (a):
          i = b
        else :
          i += 3
      elif (next_op == 6):
        if (a == 0):
          i = b
        else :
          i += 3
      elif (next_op == 7):
        if (a < b):
          data[c] = 1
        else :
          data[c] = 0
        i += 4
      elif (next_op == 8):
        if (a == b):
          data[c] = 1
        else :
          data[c] = 0
        i += 4
  
    return(program_output)

  highest = 0
  allinputs = list(itertools.permutations([0, 1, 2, 3, 4], 5))
  for x in allinputs:
    init = 0
    output = 0
    #print(x)
    for y in x:
      if (output != 0):
        init = output[0]
      output = intcode(program_data.copy(), y, init)
      #print(y, init, output)
    if (output[0] > highest or highest == 0):
      highest = output[0]
  
  return(highest)

def part2(input):
  # Will come back to part 2 later, moving on for now!
  return(1)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if (debug):
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
