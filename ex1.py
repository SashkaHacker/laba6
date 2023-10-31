#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == "__main__":
    propose = input()
    a, b = input(), input()
    print(f"Количество вхождений {a} в предложении: {propose.count(a)}")
    print(f"Количество вхождений {b} в предложении: {propose.count(b)}")
