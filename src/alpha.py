#!/usr/bin/env python
'''
Created on 18 Jul 2014

@author: henryk
'''

import gmpy2,time
rstate = gmpy2.random_state()

def get_prime(length):
    a = gmpy2.mpz_random(rstate,2<<length).bit_set(0).bit_set(length)
    while not gmpy2.is_prime(a):
        a = a+2
    return a

def generate_rsa(length):
    p = get_prime(length/2)
    q = get_prime(length - length/2)
    n = p * q
    phi_n = (p-1)*(q-1)
    e = 65537
    d = gmpy2.powmod(e, -1, phi_n)
    
    return e,d,n

if __name__ == '__main__':
    for i in range(5,13):
        start = time.time()
        e,d,n = generate_rsa(2<<i)
        stop = time.time()
        print i, (stop-start)
    
    clear = 4711
    cipher = gmpy2.powmod(clear, e, n)
    decrypt = gmpy2.powmod(cipher, d, n)
    
    print clear, decrypt