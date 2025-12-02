#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

# Постоянная Эйлера
EULER = 0.5772156649015328606
# Точность вычислений
EPS = 1e-10


if __name__ == '__main__':
    x = float(input("Введите значение x (x > 0): "))

    n = 1
    term = -(x * x) / 4
    
    series_sum = term

    while math.fabs(term) > EPS:
        numerator = -term * x * x * n
        denominator = (n + 1) * (2 * n + 1) * (2 * n + 2)
        
        term = numerator / denominator
        series_sum += term
        n += 1

    ci_val = EULER + math.log(x) + series_sum

    print(f"Ci({x}) = {ci_val}")