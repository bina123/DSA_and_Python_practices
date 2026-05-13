def is_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    
    if sorted(str1) != sorted(str2):
        return False
    
    return True

s = "rat"
t = "car"
result = is_anagram(s,t)
print(result)