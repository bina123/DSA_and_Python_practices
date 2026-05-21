from collections import defaultdict
def groupAnagrams(strs):
    if not strs:
        return ""
    
    anagrams = defaultdict(list)

    for word in strs:
        key = ' '.join(sorted(word))
        anagrams[key].append(word)
        
    return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print(result)

def groupAnagramsAnother(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        freq = [0] * 26
        
        for char in str:
            freq[ord(char) - ord('a')] += 1
            
        key = tuple(freq)
        anagrams[key].append(word)
        
    return list(anagrams.values());

strs1 = ["eat","tea","tan","ate","nat","bat"]
result1 = groupAnagrams(strs1)
print(result1)