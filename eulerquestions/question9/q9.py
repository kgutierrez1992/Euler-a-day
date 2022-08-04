#! /usr/bin/env python3
# Konnor Gutierrez
# CPSC 386
# kgutierrez1992@live.com
# 

'''This is a sample program for my CPSC 386 course'''

def main():
    '''This is the main function.'''
    
    result = 0
    a = 0
    b = 0
    c = 0
    result_arry = []
    sum_to_find = 1000

    for i in range(500):
        for j in range(i+ 1, 500):
            a = j**2 - i**2
            b = 2 * j * i
            c = j**2 + i**2

            if a + b + c > sum_to_find:
                break
            elif a + b + c == sum_to_find:
                result_arry.append(a)
                result_arry.append(b)
                result_arry.append(c)
                result = a*b*c

    print(result_arry)
    print(result)
    

if __name__ == '__main__':
    main()
