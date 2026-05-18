def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True

def get_primes(start, end):
    return [n for n in range(start,end+1) if is_prime(n)]

# Test
print(is_prime(17))  # True
print(is_prime(20))  # False
print(get_primes(1, 30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]