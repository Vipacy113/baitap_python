# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 15:34:42 2025

@author: TUF GAMING
"""
data = "tranhuuthuan22ns071@gmail.com TUE SEP 16 03:40:16"
Start_position = data.find("@")                
End_position = data.find(" ", Start_position) 
host = data[Start_position +1 : End_position]
print(host)
