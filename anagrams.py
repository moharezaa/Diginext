def group_anagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)
    
    return list(anagrams.values())

input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strs))

