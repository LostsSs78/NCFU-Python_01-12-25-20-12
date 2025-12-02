#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__"
    i = int(input("Enter number of month: "))

    if i == 1:
        print("Январь")
    elif i == 2:
        print("Февраль")
    elif i == 3:
        print("Март")
    elif i == 4:
        print("Апрель")
    elif i == 5:
        print("Май")
    elif i == 6:
        print("Июнь")
    elif i == 7:
        print("Июль")
    elif i == 8:
        print("Август")
    elif i == 9:
        print("Сентябрь")
    elif i == 10:
        print("Октябрь")
    elif i == 11:
        print("Ноябрь")
    elif i == 12:
        print("Декабрь")
    else:
        print("Something goes wrong...", file=sys.stderr)