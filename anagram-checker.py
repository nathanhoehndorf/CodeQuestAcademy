def check(w1, w2):
    if w1 == w2:
        return False
    elif sorted(w1) == sorted(w2):
        return True
    else:
        return False
    
num_test_cases = int(input())

pairs = []
for i in range(num_test_cases):
    temp_line = input()
    pairs.append(temp_line)
    
    
results = []
for pair in pairs:
    words = pair.split("|")
    if check(words[0], words[1]):
        results.append("ANAGRAM")
    else:
        results.append("NOT AN ANAGRAM")
        
for j in range(num_test_cases):
    print(pairs[j] + " = " + results[j])
    
