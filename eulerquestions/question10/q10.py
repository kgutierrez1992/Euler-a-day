#! /usr/bin/env python3
# Konnor Gutierrez
# kgutierrez1992@live.com
# 

'''This is a sample program'''

import math

def is_prime(number):
    
    for j in range(2, int(number**.5) + 1):
        if number % j == 0:
            return False
    return True

def main():
    '''This is the main function.'''
    result = 0

    number = 2000000
    for i in range(2,number):
        if is_prime(i):
            result += i

    print(result)
    

if __name__ == '__main__':
    main()
