import math

def find_distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)


num_test_cases = int(input())

master_list = []
for i in range(num_test_cases):
    coord_dist = {}
    
    num_asteroids = int(input())
    for j in range(num_asteroids):
        temp_line = input()
        
        str_coords = temp_line.split(" ")
        distance = find_distance(int(str_coords[0]), int(str_coords[1]))
        
        coord_dist.update({temp_line : distance})
        
    temp_coords = sorted(coord_dist.items(), key = lambda x:x[1])
    for coord in temp_coords:
        master_list.append(coord[0])
        
for result in master_list:
    print(result)