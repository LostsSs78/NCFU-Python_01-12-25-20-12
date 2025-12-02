#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


if __name__ == '__main__':
    a1 = int(input("Enter first coordinate: "))
    a2 = int(input("Enter second coordinate: "))
    r = int(input("Enter radius: "))

    hypot = math.sqrt(a1 ** 2 + a2 ** 2)

    if hypot <= r:
        print("Point in circle")
    elif hypot > r:
        print("Point not in cirle")
    else:
        print("Something goes wrong...", file=sys.stderr)