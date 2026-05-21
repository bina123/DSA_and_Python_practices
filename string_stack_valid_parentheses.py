def valid_paranthases(str):
    pairs = {
        "}" : "{",
        ")": "(",
        "]" : "["
    }
    
    stack = []
    
    for char in str:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
            
    return len(stack) == 0

str = "{[]}"
result = valid_paranthases(str)
print(result)

str2 = "()[]{}"
result = valid_paranthases(str2)
print(result)

str3 = "(]"
result = valid_paranthases(str3)
print(result)