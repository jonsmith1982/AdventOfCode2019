#!/usr/bin/env python3

debug = 1
if debug:
  import time
  start = time.perf_counter()

with open("challenge-01-12-2019.txt","r") as f:
  puzzle_input = [int(x.strip()) for x in f]

def part1(input):
  fuel = 0
  for x in input:
    fuel += int(x / 3) - 2
  return(fuel)

def part2(input):
  total_fuel = 0
  
  def fuel_mass_calc(mass):
    fuel = int(mass / 3) - 2
    return fuel if (fuel > 0) else 0
  
  for x in input:
    fuel = fuel_mass_calc(x)
    total_fuel += fuel
    while (fuel > 0):
      fuel = fuel_mass_calc(fuel)
      total_fuel += fuel
  
  return(total_fuel)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
