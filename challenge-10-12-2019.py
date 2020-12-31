#!/usr/bin/env python3

import math

debug = 1
if (debug):
  import time
  start_time = time.perf_counter()

asteroids = []

def angle(start, end):
  result = math.atan2(end[0] - start[0], start[1] - end[1]) * 180 / math.pi
  if (result < 0):
    return(360 + result)
  return(result)

def init_asteroids():
  asteroids = []
  with open('challenge-10-12-2019.txt') as f:
    for y, line in enumerate(f.readlines()):
      for x, a in enumerate(line):
        if (a == '#'):
          asteroids.append((x, y))
  return(asteroids)

asteroids = init_asteroids()

def part1(asteroids):

  result = None
  m = 0

  for start in asteroids:
    count = len({angle(start, end) for end in asteroids if start != end})
    if (count > m):
      m = count
      result = start

  #print('x {} y {}'.format(*result))
  print('visible {}'.format(m))
  
  return(result)

def part2(part1_result, asteroids):
  
  asteroids.remove(part1_result)
    
  angles = sorted(
    ((angle(part1_result, end), end) for end in asteroids),
    key=lambda x: (x[0], abs(part1_result[0] - x[1][0]) + abs(part1_result[1] - x[1][1]))
  )

  idx = 0
  last = angles.pop(idx)
  last_angle = last[0]
  cnt = 1

  while (cnt < 200 and angles):
    if idx >= len(angles):
      idx = 0
      last_angle = None
    if last_angle == angles[idx][0]:
      idx += 1
      continue
    last = angles.pop(idx)
    last_angle = last[0]
    cnt += 1
  #print('vaporized {}: {} {}'.format(cnt, last[1], last[1][0] * 100 + last[1][1]))
    
  return(last[1][0] * 100 + last[1][1])

part1_result = part1(asteroids)

print("Part I :", part1_result)
print("Part II:", part2(part1_result, asteroids))

if (debug):
  end_time = time.perf_counter()
  print("Runtime: {:5.3f}".format(end_time - start_time))
