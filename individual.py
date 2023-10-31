#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == "__main__":
    word1, word2, word3 = input(), input(), input()
    letters = set(word1) & set(word2) & set(word3)
    if letters:
        print(*letters)
    else:
        print("Одинаковых букв нет")
