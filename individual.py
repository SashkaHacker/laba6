#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == "__main__":
    word1, word2, word3 = input(), input(), input()
    lst1 = [i for i in word1]
    lst2 = [i for i in word2]
    lst3 = [i for i in word3]
    letters = set(lst1) & set(lst2) & set(lst3)
    if letters:
        print(*letters)
    else:
        print("Одинаковых букв нет")
