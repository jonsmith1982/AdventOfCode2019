#!/usr/bin/env python3

debug = 1
if debug:
  import time
  start = time.perf_counter()

with open("challenge-06-12-2019.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  orbit_map = dict()
  
  for x in input:
    planets = x.split(')')
    if (planets[1] in orbit_map):
      orbit_map[planets[1]].append(planets[0])
    else :
      orbit_map[planets[1]] = [planets[0]]
  
  def trackback(planet):
    count = 0
    queue = []
    while (planet in orbit_map):
      count += 1
      planets = orbit_map[planet]
      if (len(planets) > 1):
        queue += planets[1:]
      planet = planets[0]
      if (planet not in orbit_map and len(queue) > 0):
        planet = queue.pop(0)
    return(count)
  
  total = 0
  for x in orbit_map:
    total += trackback(x)
  
  return(total)

def part2(input):
  orbit_map = dict()
  
  for x in input:
    planets = x.split(')')
    if (planets[1] in orbit_map):
      orbit_map[planets[1]].append(planets[0])
    else :
      orbit_map[planets[1]] = [planets[0]]
  
  def trackback(planet):
    history = []
    while (planet in orbit_map):
      planets = orbit_map[planet]
      if (len(planets) > 1):
        queue += planets[1:]
      planet = planets[0]
      history.append(planet)
    return(history)
  
  youhistory = trackback('YOU')
  sanhistory = trackback('SAN')
  allhistory = list(set(youhistory.copy()) & set(sanhistory.copy()))

  closest = 0
  for x in allhistory:
    if (x == 'COM'):
      continue
    youindex = youhistory.index(x)
    sanindex = sanhistory.index(x)
    if (youindex + sanindex < closest or closest == 0):
      closest = youindex + sanindex
  
  return(closest)
  
print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
