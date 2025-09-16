# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 20:47:35 2025

@author: TUF GAMING
"""

import math

a = float(input("Nhập cạnh tam giác đều: "))

# Diện tích theo Bài 7
A = B = C = math.pi / 3
S_bai7 = 0.5 * a * a * math.sin(C)

# Diện tích theo Bài 8
S_bai8 = (a**2 * math.sqrt(3)) / 4

print("Diện tích tính theo Bài 7:", S_bai7)
print("Diện tích tính theo Bài 8:", S_bai8)
