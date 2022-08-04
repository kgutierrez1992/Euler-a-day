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
    found = False
    result = 1
    while found == False:
        if result % 20 == 0 and result % 19 == 0 and result % 18 == 0 and result % 17 == 0 and result % 16 == 0 and result % 15 == 0 and result % 14 == 0 and result % 13 == 0 and result % 12 == 0 and result % 11 == 0:
            break
        else:
            result += 1

    print(result)




    

if __name__ == '__main__':
    main()
