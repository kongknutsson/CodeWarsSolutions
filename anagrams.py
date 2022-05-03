"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

"""

# Solution 1
def anagrams(word, words):
    word_freq = freq(word)
    res = []
    for curr_word in words:
        if freq(curr_word) == word_freq:
            res.append(curr_word)
    return res
    
def freq(word):
    cnt = {}
    for letter in word:
        if letter not in cnt:
            cnt[letter] = 1
        else:
            cnt[letter] += 1
    return cnt
        
# Solution 2
def anagrams_2(word, words):
    anagrams = []
    for possible_word in words:
        curr = possible_word
        possible_word = list(possible_word)
        if len(word) != len(possible_word):
            continue
        for letter in word:
            if letter in possible_word:
                possible_word.pop(possible_word.index(letter))
            if len(possible_word) == 0:
                anagrams.append(curr)
    return anagrams