import math

def find_distance(alt):
    radius = 40075 / (2 * math.pi)
    circumference = 2 * math.pi * (radius + alt)
    return round(circumference, 1)

num_test_cases = int(input())

altitudes = []
for _ in range(num_test_cases):
    num_temp = input()
    altitudes.append(int(num_temp))
    
for altitude in altitudes:
    print(find_distance(altitude))
