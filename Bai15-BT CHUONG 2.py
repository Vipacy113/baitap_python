# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 21:22:25 2025

@author: TUF GAMING
"""

# Nhiệt dung riêng của nước
C = 4.186  # J/g°C

# Nhập dữ liệu
M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập độ thay đổi nhiệt độ ΔT (°C): "))

# Tính năng lượng Q (Joules)
Q = M * C * delta_T

# Đổi sang kWh
Q_kWh = Q * 2.777e-7

# Chi phí (8.9 cent mỗi kWh)
cost = Q_kWh * 8.9

print(f"Năng lượng cần: {Q:.2f} Joules")
print(f"Đổi sang kWh: {Q_kWh:.8f} kWh")
print(f"Chi phí để đun nóng: {cost:.4f} cent")
