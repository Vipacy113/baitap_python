# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 21:25:25 2025

@author: TUF GAMING
"""

import math

# Nhập dữ liệu
Ta = float(input("Nhập nhiệt độ không khí (°C): "))
V = float(input("Nhập tốc độ gió (km/h): "))

# Công thức tính WCI
WCI = 13.12 + 0.6215 * Ta - 11.37 * (V ** 0.16) + 0.3965 * Ta * (V ** 0.16)

# Làm tròn số nguyên gần nhất
WCI_rounded = round(WCI)

print("Chỉ số gió lạnh (WCI) là:", WCI_rounded)
