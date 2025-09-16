# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 15:52:52 2025

@author: TUF GAMING
"""

import math

r = float(input("Nhập bán kính đáy r: "))
h = float(input("Nhập chiều cao h: "))

V = math.pi * r**2 * h

print(">>> Thể tích hình trụ với r =", r, "và h =", h, "là:", V)
