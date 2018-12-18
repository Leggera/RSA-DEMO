import math


def gcd(x, y):  
    if x == 0:
        return y
    return gcd(y % x, x)

def euler_function(n):
    num = 1 # initialization, because there's always a 1
    for _ in range(2, n):
        if gcd(n, _) == 1:
            num += 1
    return num

def fast_pow(x, n, mod=0):
    if n < 0:
        return fast_pow(1/x, -n, mod=mod)
    if n == 0:
        return 1
    if n == 1:
        if mod == 0:
            return x
        else:
            return x % mod
    if n % 2 == 0:
        if mod == 0:
            return fast_pow(x * x,  n / 2, mod=mod)
        else:
            return fast_pow(x * x,  n / 2, mod=mod) % mod
    else:
        if mod == 0:
            return x * fast_pow(x * x, (n - 1) / 2, mod=mod)
        else:
            return x * fast_pow(x * x, (n - 1) / 2, mod=mod) % mod

def discrete_log(a, b, p):
    """
    In this function we are using an assumption that p is a prime number
    """
    H = math.ceil(math.sqrt(p-1))
    
    hash_table = {fast_pow(a, i, p) : i for i in range(H)}
    
    c = fast_pow(a, H * (p - 2), p)
    
    for j in range(H):
        x = (b * fast_pow(c, j, p)) % p
        if x in hash_table:
            return j * H + hash_table[x]
        
    return None 
