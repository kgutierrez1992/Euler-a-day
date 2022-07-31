#! /usr/bin/env python3
# Konnor Gutierrez
# CPSC 386
# kgutierrez1992@live.com
# 

def main():
    '''This is the main function.'''
    print("hello world")
    

if __name__ == '__main__':
    main()




def main():
    """This module prints 'Hello World!'."""
    print("Hello World!")
    first_n_natural = 100

    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, first_n_natural + 1):
        sum_of_squares +=  i**2
        square_of_sum += i
    square_of_sum = square_of_sum**2

    print(square_of_sum - sum_of_squares)


if __name__ == '__main__':
    main()
