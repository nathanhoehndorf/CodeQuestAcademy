vowels = {
    
    'a' : 'v',
    'e' : 'v',
    'i' : 'v',
    'o' : 'v',
    'u' : 'v'
    
}

def numVowels(str):
    sum = 0
    for s in str:
        if vowels.get(s) == 'v':
            sum += 1
        
        
    return sum

num_test_cases = int(input())

sentences = []
for i in range(num_test_cases):
    temp_line = input()
    sentences.append(temp_line)
    
    
results = []
for sentence in sentences:
    out = numVowels(sentence)
    results.append(out)
    
for result in results:
    print(result)
    
