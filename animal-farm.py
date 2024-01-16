def numLegs(turkey, goat, horse):
    sum = 0
    sum += (turkey * 2)
    sum += (goat * 4)
    sum += (horse * 4)
    return sum

num_test_cases = int(input())

inputs = []
for i in range(num_test_cases):
    inputs.append(input())
    
results = []
for input in inputs:
    nums = input.split(" ")
    results.append(numLegs(int(nums[0]), int(nums[1]), int(nums[2])))
    
for result in results:
    print(result)