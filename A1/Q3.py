# COMP 424 - Assignment #1 (Winter 20201)
# Emmanuelle Coutu-Nadeau
# ID: 260681550
#
# References:
# https://en.wikipedia.org/wiki/2-opt#:~:text=In%20optimization%2C%202%2Dopt%20is,already%20been%20suggested%20by%20Flood
# https://towardsdatascience.com/how-to-implement-the-hill-climbing-algorithm-in-python-1c65c29469de

import random
import math
import statistics 
from itertools import permutations 
from itertools import combinations 

optimal_paths = []
random_paths = []

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

# Function to generate n TSP problems
def generate_tsp_data (n, cities):
  data = []
  for i in range(n):
    g = []
    for j in range(cities):
      x = random.uniform(0, 1)
      y = random.uniform(0, 1)
      g.append([x, y])
    data.append(g)
  return data

def dist (p1, p2):
  distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
  return distance

def tour_length(tour):
  l = 0
  p1 = tour[0] # start with the first city
  for city in tour:
    l += dist(p1, city)
    p1 = city
  return l

def brute_TSP (data):
  global optimal_paths
  result = {}
  best_length = 0
  result['lengths'] = []
  # for each instance
  for tsp in data:
    # list all possible permutations (i.e. tours including all cities exactly once)
    perm = permutations(tsp) 
    for tour in perm:
      l = tour_length(tour)
      if (best_length > l or best_length == 0):
        best_length = l
    result['lengths'].append(best_length)
    optimal_paths.append(best_length)

  mean = statistics.mean(result['lengths'])
  sd = statistics.stdev(result['lengths'])
  max_length = max(result['lengths'])
  min_length = min(result['lengths'])

  result['mean'] = mean
  result['min'] = min_length
  result['max'] = max_length
  result['sd'] = sd

  return result

# Question 3 b)
def random_path_selection(data):
  global optimal_paths, random_path_selection
  result = {}
  nb_optimal = 0
  result['lengths'] = []
  # for each instance
  for i in range(len(data)):
    # Select a random tour
    tour = data[i]
    random_paths.append(tour)
    l = tour_length(tour)
    result['lengths'].append(l)
    if (l in optimal_paths):
      nb_optimal += 1

  mean = statistics.mean(result['lengths'])
  sd = statistics.stdev(result['lengths'])
  max_length = max(result['lengths'])
  min_length = min(result['lengths'])

  result['mean'] = mean
  result['min'] = min_length
  result['max'] = max_length
  result['sd'] = sd
  return nb_optimal, result

# Question 3 c) Hill climbing
def extract_from_list(list, range):
  sublist = list[range[0], range[1]+1]
  return sublist

def two_opt_swap(route, i, k):
  new_route = []

  range_list = [(0,i), (i,k), (k, len(route))]
  
  a = route[range_list[0][0]:range_list[0][1]]
  b = route[range_list[1][0]:range_list[1][1]]
  b.reverse()
  c = route[range_list[2][0]:range_list[2][1]]

  for el in a:
    new_route.append(el)
  for el in b:
    new_route.append(el)
  for el in c:
    new_route.append(el)

  return new_route

def get_best_swap(route, nb_cities):
  new_route = []
  # nb_of_possible_swaps = nCr(nb_cities, 2)
  comb = combinations(range(nb_cities), 2)
  for c in comb:
    best_distance = tour_length(route)
    new_route = two_opt_swap(route, c[0], c[1])
    new_distance = tour_length(new_route)
    if(new_distance < best_distance):
      route = new_route
      best_distance = new_distance
  return new_route

def hill_climbing(random_selection, nb_cities):
  global optimal_paths

  result = {}
  nb_optimal = 0
  result['lengths'] = []
  index = 0

  # for each instance
  for tour in random_selection:
    l = tour_length(tour)
    best_neighbours = get_best_swap(tour, nb_cities)
    best_length = tour_length(best_neighbours)

    while best_length < l:
      tour = best_neighbours
      l = best_length
      best_neighbours = get_best_swap(tour, nb_cities)
      best_length = tour_length(best_neighbours)
      # if (best_length <= l):
      #   break
    
      if (best_length in optimal_paths):
        nb_optimal += 1

    result['lengths'].append(best_length)

    index += 1

  mean = statistics.mean(result['lengths'])
  sd = statistics.stdev(result['lengths'])
  max_length = max(result['lengths'])
  min_length = min(result['lengths'])

  result['mean'] = mean
  result['min'] = min_length
  result['max'] = max_length
  result['sd'] = sd

  return nb_optimal, result


def main():
  global random_paths

  # Creating 100 instances of TSP with 7 cities
  instances = generate_tsp_data(100, 7)

  # Results for Question 3 a)
  res1 = brute_TSP(instances)
  print("7 cities optimal")
  print("Mean: ",res1['mean'])
  print("Max: ",res1['max'])
  print("Min: ",res1['min'])
  print("SD: ",res1['sd'])
  print('\n')

  # Results for Question 3 b)
  nb_optimal, res2 = random_path_selection(instances)
  print("7 cities - random paths")
  print("Mean: ", res2['mean'])
  print("Max: ", res2['max'])
  print("Min: ", res2['min'])
  print("SD: ", res2['sd'])
  print("# optimal: ", nb_optimal)
  print('\n')

  # Results for Question 3 c)
  nb_optimal, res3 = hill_climbing(random_paths, 7)
  print("7 cities - Hill climbing")
  print("Mean: ", res3['mean'])
  print("Max: ", res3['max'])
  print("Min: ", res3['min'])
  print("SD: ", res3['sd'])
  print("# optimal: ", nb_optimal)
  print('\n')

  # Results for Question 3 d)
  instances_scaledup = generate_tsp_data(100, 100)
  random_paths = [] #reset random_paths

  nb_optimal, res4 = random_path_selection(instances_scaledup)
  print("100 cities - random paths")
  print("Mean: ", res4['mean'])
  print("Max: ", res4['max'])
  print("Min: ", res4['min'])
  print("SD: ", res4['sd'])
  print("# optimal: ", nb_optimal)
  print('\n')

  nb_optimal, res5 = hill_climbing(random_paths, 100)
  print("100 cities - Hill climbing")
  print("Mean: ", res5['mean'])
  print("Max: ", res5['max'])
  print("Min: ", res5['min'])
  print("SD: ", res5['sd'])
  print('\n')

main()

