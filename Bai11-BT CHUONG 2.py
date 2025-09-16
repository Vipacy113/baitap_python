# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 20:50:26 2025

@author: TUF GAMING
"""

width = float(input("Nhập chiều rộng (m): "))
length = float(input("Nhập chiều dài (m): "))

area_m2 = width * length
area_acre = area_m2 / 43560

print("Diện tích cánh đồng là:", area_acre, "mẫu Anh")
