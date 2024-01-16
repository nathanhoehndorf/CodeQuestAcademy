def hamming_distance(word1, word2):
    if len(word1) != len(word2):
        return -1
    
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
            
    return distance

def determine_closest_match(miss_word, correct_words):
    distances = []
    for word in correct_words:
        distances.append(hamming_distance(word, miss_word))
        
    max_dist = max(distances)
    for i in range(len(distances)):
        if distances[i] != -1:
            return correct_words[i]


num_test_cases = int(input())

for _ in range(num_test_cases):
    temp_in = input().split(" ")
    
    num_dict_words = int(temp_in[0])
    num_miss_words = int(temp_in[1])
    
    dict_words = []
    for _ in range(num_dict_words):
        dict_words.append(input())
        
    miss_words = []
    for _ in range(num_miss_words):
        miss_words.append(input())
        
    
    for word in miss_words:
        print(determine_closest_match(word, dict_words))
 
    