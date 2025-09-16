# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 21:21:44 2025

@author: TUF GAMING
"""

import math

# Nhập số nguyên từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Thực hiện các phép toán
tong = a + b
hieu = a - b
tich = a * b

# Chia và chia lấy dư (kiểm tra tránh chia cho 0)
if b != 0:
    thuong = a / b
    phan_du = a % b
else:
    thuong = "Không xác định (chia cho 0)"
    phan_du = "Không xác định (chia cho 0)"

# log10(a) (kiểm tra a > 0 mới tính log)
if a > 0:
    log_a = math.log10(a)
else:
    log_a = "Không xác định (a <= 0)"

# a^b
luy_thua = a ** b

# Hiển thị kết quả
print("Tổng của a và b =", tong)
print("Hiệu của a và b =", hieu)
print("Tích của a và b =", tich)
print("Thương của a chia b =", thuong)
print("Phần còn lại khi a chia b =", phan_du)
print("Kết quả log10(a) =", log_a)
print("Kết quả a^b =", luy_thua)
