import math
from random import randint

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
            
def egcd(a, b):
    if (a == 0):
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_big_prime(n, test_count=1000):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, test_count):
            return p
        
def generate_modulo(bitlen, tc=1000):       
    p = generate_big_prime(bitlen//2, tc)                          
    q = 1
    n = p * q  
    while (math.ceil(math.log(n, 2)) != bitlen):
        q = generate_big_prime(bitlen - bitlen//2, tc)
        n = p * q

    return  n, (p-1)*(q-1)

def rsa_generate_keys(bitlen, tc=1000):
    '''
    inputs:
    bitlen - bitwise size of the keys
    tc - number of iterations for cheking the primality
    returns:
    private_key: (modulo, exponent), public_key: (modulo, exponent)
    '''
    n, phi = generate_modulo(bitlen, tc)
    k = randint(bitlen//12, bitlen//20)
    e = 2**k + 2 * randint( 2**(k//8), 2**(k//4) ) + 1 # a common convention to generate public exponent first
    g, x, y = egcd(e, phi)
    d = x % phi
    while (g != 1):
        e = 2**k + 2 * randint( 2**(k//8), 2**(k//4) ) + 1
        g, x, y = egcd(e, phi)
        d = x % phi
    return (n, d), (n, e)

def rsa_encrypt(public_key, message, modulo):
    return fast_pow(message, public_key, modulo)

def rsa_decrypt(private_key, message, modulo):
    return fast_pow(message, private_key, modulo)

def rsa_sign(private_key, h, modulo):
    '''
    h - hash
    '''
    return fast_pow(h, private_key, modulo)

def rsa_check(public_key, h, g, modulo):
    '''
    h - received hash value
    g - computed hash value
    '''
    return fast_pow(h, public_key, modulo) == g
