#! /usr/bin/env python3
# Konnor Gutierrez
# CPSC 386-01
# 2022-07-10
# kgutierrez1992@live.com
# @kgutierrez1992
#
# Lab 00-00
#
# This is my first python program. It prints "Hello World!"
#


def is_even(n):
    return n % 2 == 0

def main():
    sum = 2
    a = 1
    b = 2
    next = 0
    max_val = 4000000
    while (a + b) < max_val:
        print(a + b)
        next = a + b
        if is_even(next):
            print("i am even")
            sum += a + b
        a = b
        b = next
    print(sum)
        

if __name__ == '__main__':
    main()
