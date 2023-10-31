#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == "__main__":
    propose = input()
    letter = input()
    ind = propose.rindex("и")
    match ind:
        case 0:
            propose = letter + propose[ind:]
        case _:
            propose = propose[:ind] + letter + propose[ind:]
    print(propose)
