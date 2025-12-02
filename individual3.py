#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    d = int(input("Введите день (d): "))
    m = int(input("Введите месяц (m): "))
    y = int(input("Введите год (y): "))

    days_in_feb = 28
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        days_in_feb = 29

    day_number = d

    for month in range(1, m):
        if month == 2:
            day_number += days_in_feb
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day_number += 30
        else:
            day_number += 31

    print(f"Порядковый номер даты: {day_number}")