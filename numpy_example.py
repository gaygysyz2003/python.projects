# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 12.12
# Date: 11/18/2023

import numpy as np
# As a team, we have gone through all required sections of the # tutorial, and each team member understands the material
import math
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
print(f'A = {a}')

b = np.array([[0, 1],
              [2, 3],
              [4, 5],
              [6, 7]])

print(f'B = {b}')
c = np.array([[0, 1, 2],
             [3, 4, 5]])
print(f'C = {c}')


d = a @ b @ c
print(f'D = {d}')

e = d.transpose()
print(f'D^T = {e}')

f = np.sqrt(d) / 2

print(f'E = {f}')