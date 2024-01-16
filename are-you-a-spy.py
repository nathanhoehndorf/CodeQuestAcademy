import string

def format_phrase(phrase1, phrase2):
    # lower-case the text
    phrase1 = phrase1.lower()
    phrase2 = phrase2.lower()
    
    # strip the text of punctuation
    phrase1 = phrase1.translate(str.maketrans('', '', string.punctuation))
    phrase2 = phrase2.translate(str.maketrans('', '', string.punctuation))
    
    return phrase1, phrase2



def check_code(phrase1, phrase2):
    phrase1, phrase2 = format_phrase(phrase1, phrase2)
    characters = {}
    for i in range(len(phrase1)):
        curr_char_val = characters.get(phrase1[i])
        if curr_char_val != None:
            characters.update({phrase1[i] : (curr_char_val) + 1})
        else:
            characters.update({phrase1[i] : 1})
            
    for j in range(len(phrase2)):
        curr_char_val2 = characters.get(phrase2[j])
        if curr_char_val2 == None:
            return "You're not a secret agent!"
        
    return "That's my secret contact!"

num_test_cases = int(input())

word_pairs = []
for i in range(num_test_cases):
    word_pairs.append(input())
    
    
results = []
for word_pair in word_pairs:
    words = word_pair.split("|")
    results.append(check_code(words[0], words[1]))
    
    
for result in results:
    print(result)
    
