#!/usr/bin/env python3

debug = 1
if (debug):
  import time
  start_time = time.perf_counter()

with open("challenge-08-12-2019.txt", "r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  width = 25
  height = 6
  layers = int(len(input[0]) / (width * height))
  
  least_layer = 0
  result = 0
  
  for l in range(layers):
    zero_count, one_count, two_count = 0, 0, 0
    start = l * (width * height)
    end = start + (width * height)
    for i in range(start, end):
      if (input[0][i] == '0'):
        zero_count += 1
      elif (input[0][i] == '1'):
        one_count += 1
      elif (input[0][i] == '2'):
        two_count += 1
    if (zero_count < least_layer or least_layer == 0):
      least_layer = zero_count
      result = one_count * two_count 
  
  return(result)

def part2(input):
  width = 25
  height = 6
  layers = int(len(input[0]) / (width * height))
  
  image = []
  
  for l in range(layers):
    i = l * (width * height)
    for h in range(height):
      row = []
      for w in range(width):
        row.append(input[0][i])
        if (l != 0):
          if (image[h][w] == '2' and input[0][i] != '2'):
            image[h][w] = input[0][i]
        i += 1
      if (l == 0):
        image.append(row)
  
  return('RKHRY')

print("Part I :", part1(puzzle_input))
print("Part II:", part2(puzzle_input))

if (debug):
  end_time = time.perf_counter()
  print("Runtime: {:5.3f}".format(end_time - start_time))