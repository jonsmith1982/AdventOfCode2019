#!/usr/bin/env python3

debug = 1
if debug:
  import time
  start = time.perf_counter()

with open("challenge-05-12-2019.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  data = [int(x) for x in input[0].split(',')]
  program_input = [1]
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
      data[a] = program_input[-1]
      i += 2
    elif (next_op == 4):
      program_output.append(a)
      i += 2

  return(program_output)

def part2(input):
  data = [int(x) for x in input[0].split(',')]
  program_input = [5]
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
    if (ap == 0 and next_op != 3):
      a = data[a]
    if (len(data) > i + 2):
      b = data[i + 2]
      if (bp == 0):
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
      data[a] = program_input[-1]
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

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
