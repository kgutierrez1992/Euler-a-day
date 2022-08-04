#! /usr/bin/env python3
# Konnor Gutierrez
# CPSC 386
# kgutierrez1992@live.com
# 

'''This is a sample program for my CPSC 386 course'''

def is_prime(number, i):
    return number % i == 0

def main():
    '''This is the main function.'''
    prime_array = [2, 3]
    number = 3
    while len(prime_array) < 10001:
        for i in range(2, (number // 2) + 1):
            if is_prime(number, i):
                break
            elif i == number // 2:
                prime_array.append(number)
        number += 1
    print(prime_array[10000])
    

if __name__ == '__main__':
    main()
