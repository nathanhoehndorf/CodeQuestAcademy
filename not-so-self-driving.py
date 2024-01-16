def determine_action(v, x):
    if v == 0:
        return 'SAFE'
    
    time_to_collide = x / v
    if time_to_collide <= 1:
        return 'SWERVE'
    elif time_to_collide <= 5:
        return 'BRAKE'
    else:
        return 'SAFE'
    

num_test_cases = int(input())

test_cases = []
for i in range(num_test_cases):
    temp_case = input()
    test_cases.append(temp_case)
    
    
output = []
for case in test_cases:
    nums = case.split(":")
    out = determine_action(float(nums[0]), float(nums[1]))
    output.append(out)
        

for x in output:
    print(x)
