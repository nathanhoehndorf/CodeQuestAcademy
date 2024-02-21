bats = {
    
    'K' : 0,
    '1B' : 1,
    '2B' : 2,
    '3B' : 3,
    'HR' : 4
    
}

def slg( k, s, d, t, hr):
    single = s
    double = 2 * d
    triple = 3 * t
    home_run = 4 * hr
    
    den = k + s + d + t + hr
    num = single + double + triple + home_run
    
    return num / den


def sort_bats(str):
    bat_str = str[str.find(':') + 1:]
    bats = bat_str.split(",")
    
    return bats
    

num_test_cases = int(input())

inputs = []
for _ in range(num_test_cases):
    inputs.append(input())
    
for input in inputs:
    bat_results = sort_bats(input)
    

    
    
