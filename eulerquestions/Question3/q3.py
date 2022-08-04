#! /usr/bin/env python3
# Konnor Gutierrez
# CPSC 386
# kgutierrez1992@live.com
# 

'''This is a sample program for my CPSC 386 course'''

def is_divisible(dividend, divisor):
    return dividend % divisor == 0


def main():
    '''This is the main function.'''
    original = 600851475143
    max_val = 600851475143
    n = 1
    while n < max_val:
        if is_divisible(max_val, n):
            max_val = max_val // n
        n += 1
    print(f"The largest prime value for {original} is: {max_val}")



if __name__ == '__main__':
    main()
