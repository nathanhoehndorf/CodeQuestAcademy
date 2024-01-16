def addiply(a, b):
    sum = a + b
    product = a * b
    return f"{sum} {product}"

num_test_cases = int(input())

results = []

for i in range(num_test_cases):
    nums = input().split(" ")
    out = addiply(int(nums[0]), int(nums[1]))
    results.append(out)
    
for result in results:
    print(result)