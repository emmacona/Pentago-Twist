import random
import math
import statistics 
from itertools import permutations 
from itertools import combinations 

# Function to generate TSP problem
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

def naive_TSP (data):
  result = {}
  best_length = 0
  best_path = []
  result['lengths'] = []
  # for each instance
  for graph in data:
    # list all possible permutations (i.e. tours including all cities exactly once)
    perm = permutations(graph) 
    for tour in perm:
      l = tour_length(tour)
      if (best_length < l or best_length == 0):
        best_length = l
        best_path = tour
      result['lengths'].append(l)

  mean = statistics.mean(result['lengths'])
  sd = statistics.stdev(result['lengths'])
  max_length = max(result['lengths'])
  min_length = min(result['lengths'])

  result['mean'] = mean
  result['min'] = min_length
  result['max'] = max_length
  result['sd'] = sd
  return best_path, result

# Question 3 b)
def random_path_selection(data, best_path):
  result = {}
  nb_optimal = 0
  result['lengths'] = []
  # for each instance
  for graph in data:
    # Select a random tour
    perm = list(permutations(graph))
    tour = random.choice(perm)
    l = tour_length(tour)
    if (tour == best_path):
      nb_optimal += 1
    result['lengths'].append(l)

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
def get_neighbours(path, combination_range):   
  neighbours = []
  swaps = combinations(range(combination_range), 2)
  for s in swaps:
      neighbour = path
      pos1, pos2 = s[0], s[1]
      neighbour[pos1][0] = path[pos2][0]
      neighbour[pos1][1] = path[pos2][1]
      neighbour[pos2][0] = path[pos1][0]
      neighbour[pos2][1] = path[pos1][1]
      neighbours.append(neighbour)
  return neighbours

def get_best_neighbours(graph, neighbours, l):
  best_length = l
  best_neighbours = neighbours
  for n in neighbours:
    current_length = tour_length(n)
    if (current_length < best_length and current_length != 0):
      best_length = current_length
      best_neighbours = n
  return best_length, best_neighbours

def hill_climbing(data, nb_cities, best_path):
  result = {}
  nb_optimal = 0
  result['lengths'] = []
  # for each instance
  for graph in data:
    # Select a random tour
    perm = list(permutations(graph))
    tour = random.choice(perm)
    l = tour_length(tour)
    neighbours = get_neighbours(tour, nb_cities)
    best_length, best_neighbours = get_best_neighbours(graph, neighbours, l)
    
    while best_length < l:
      tour = best_neighbours
      l = best_length
      neighbours = get_neighbours(tour, nb_cities)
      best_length, best_neighbours = get_best_neighbours(graph, neighbours, l)

    result['lengths'].append(best_length)

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
  # Creating 100 instances of TSP with 7 cities
  instances = generate_tsp_data(100, 7)

  # Results for Question 3 a)
  best, res1 = naive_TSP(instances)
  print("Q3 A)")
  print("Mean: ",res1['mean'])
  print("Max: ",res1['max'])
  print("Min: ",res1['min'])
  print("SD: ",res1['sd'])
  print('\n')

  # Results for Question 3 b)
  nb_optimal, res2 = random_path_selection(instances, best)
  print("Q3 B)")
  print("Mean: ", res2['mean'])
  print("Max: ", res2['max'])
  print("Min: ", res2['min'])
  print("SD: ", res2['sd'])
  print("# optimal: ", nb_optimal)
  print('\n')

  # Results for Question 3 c)
  nb_optimal, res3 = hill_climbing(instances, 7, best)
  print("Q3 C)")
  print("Mean: ", res3['mean'])
  print("Max: ", res3['max'])
  print("Min: ", res3['min'])
  print("SD: ", res3['sd'])
  print("# optimal: ", nb_optimal)
  print('\n')

  # # Results for Question 3 d)
  instances_scaledup = generate_tsp_data(100, 100)

  nb_optimal, res4 = random_path_selection(instances_scaledup, best)
  print("Q3 D) - Random path selection")
  print("Mean: ", res4['mean'])
  print("Max: ", res4['max'])
  print("Min: ", res4['min'])
  print("SD: ", res4['sd'])
  print("# optimal: ", nb_optimal)
  print('\n')

  nb_optimal, res5 = hill_climbing(instances_scaledup, 15, best)
  print("Q3 D) - Hill climbing")
  print("Mean: ", res5['mean'])
  print("Max: ", res5['max'])
  print("Min: ", res5['min'])
  print("SD: ", res5['sd'])
  print("# optimal: ", nb_optimal)
  print('\n')

main()