#!/usr/bin/env python3

debug = 1
if debug:
  import time
  start = time.perf_counter()

puzzle_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]

def part1(input):
  input[1] = 12
  input[2] = 2
  
  for i in range(0, len(input), 4):
    op = input[i]
    if (op == 1):
      a = input[i + 1]
      b = input[i + 2]
      c = input[i + 3]
      input[c] = input[a] + input[b]
    elif (op == 2):
      a = input[i + 1]
      b = input[i + 2]
      c = input[i + 3]
      input[c] = input[a] * input[b]
    elif (op == 99):
      break

  return(input[0])

def part2(input):
  
  def run_intcode(noun, verb):
    intcode = input.copy()
    intcode[1] = noun
    intcode[2] = verb
    for i in range(0, len(intcode), 4):
      op = intcode[i]
      if (op == 1):
        a = intcode[i + 1]
        b = intcode[i + 2]
        c = intcode[i + 3]
        intcode[c] = intcode[a] + intcode[b]
      elif (op == 2):
        a = intcode[i + 1]
        b = intcode[i + 2]
        c = intcode[i + 3]
        intcode[c] = intcode[a] * intcode[b]
      elif (op == 99):
        break
    return(intcode[0])

  target = 19690720
  result = 0
  
  answer = [0, 0]
  
  while (result != target):
    for i in range(100):
      answer[0] = i
      for x in range(100):
        answer[1] = x
        result = run_intcode(i, x)
        if (result == target):
          break
      if (result == target):
        break

  return(100 * answer[0] + answer[1])

print("PartI:", part1(puzzle_input.copy()))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
