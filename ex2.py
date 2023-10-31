#!/usr/bin/env pyhton3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == "__main__":
    propose = input()
    propose = propose.replace("чя", "ча")
    propose = propose.replace("щя", "ща")
    print(propose)