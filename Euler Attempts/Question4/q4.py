#! /usr/bin/env python3
# Konnor Gutierrez
# CPSC 386
# kgutierrez1992@live.com
# 

'''This is a sample program for my CPSC 386 course'''

def main():
    """This module prints 'Hello World!'."""
    max = 0
    for val_one in range(999, 99, -1):
        for val_two in range(val_one, 100, -1):
            product = val_one * val_two
            reverse = str(product)[::-1]
            if str(product) == reverse:
                if product >= max:
                    max = product
    print(max)
if __name__ == '__main__':
    main()