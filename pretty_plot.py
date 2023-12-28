# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 12.13
# Date: 11/18/2023

import numpy as np
import matplotlib.pyplot as plt

point = np.array([0, 1])

matrix_start = np.array([[1.02, 0.095], [-0.095, 1.02]])

vector = matrix_start @ point

point = vector

points = []
points.append(vector.tolist())

# print(points)
# make for loop to repeat multiplying process 250 times
for i in range(249):
    vectors = matrix_start @ point
    point = vectors
    points.append(vectors.tolist())



x = []
y = []

for i in points:
    x.append(i[0])

for j in points:
    y.append(j[1])


plt.scatter(x, y)
plt.title('Inward swirl graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()