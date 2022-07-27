#! /usr/bin/env python3
# Konnor Gutierrez
# CPSC 386-01
# 2022-07-15
# kgutierrez1992@live.com
# @kgutierrezCSUF
#
# Quiz 02-00
#
# This is my first python program. It prints "Hello World!"
#

"""This module performs the Hello World program."""


def main():
    """This is the main program. It is the entry point for this program."""

    values = []
    solution = 0

    for num in range(1, 1000):
        if num % 3 == 0 or num % 5 == 0:
            values.append(num)

    for val in values:
        solution += val

    print(f"The sum of all multiples of 3 and 5 from 1 to 1000 is: {solution}")


if __name__ == "__main__":
    main()
