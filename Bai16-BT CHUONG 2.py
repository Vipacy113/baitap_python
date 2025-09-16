# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 21:25:09 2025

@author: TUF GAMING
"""
import math

# Gia tốc trọng trường
a = 9.8  # m/s^2

# Nhập chiều cao
d = float(input("Nhập chiều cao (m): "))

# Tính vận tốc cuối cùng
v_f = math.sqrt(2 * a * d)

print(f"Vận tốc khi chạm đất là: {v_f:.2f} m/s")
