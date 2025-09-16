# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 21:16:28 2025

@author: TUF GAMING
"""

meal_cost = float(input("Nhập chi phí bữa ăn: "))

tip = meal_cost * 0.18
tax = meal_cost * 0.05
total = meal_cost + tip + tax

print(f"Tiền bữa ăn: {meal_cost:.2f}")
print(f"Tiền thuế (5%): {tax:.2f}")
print(f"Tiền boa (18%): {tip:.2f}")
print(f"Tổng cộng phải trả: {total:.2f}")
