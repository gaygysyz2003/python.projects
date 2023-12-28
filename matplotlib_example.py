# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gaygysyz Satlykov
# Section: 521
# Assignment: Lab 12.13
# Date: 11/18/2023
import matplotlib.pyplot as plt
import numpy as np
import math
# As a team, we have gone through all required sections of the # tutorial, and each team member understands the material
def num_1():
    x = np.linspace(-2, 2,)
    y1 = (1 / (4 * 2)) * x ** 2
    y2 = (1 / (4 * 6)) * x ** 2

    plt.plot(x, y1, color='red', linewidth = 2.0, label = 'f=2')
    plt.plot(x, y2, color='blue', linewidth = 6.0, label = 'f=6')
    plt.title('Parabola plots with varying focal length')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


num_1()
def stars():
    x = np.linspace(-4,4, 25)
    y1 = (2 * x ** 3) + (3 * x ** 2) - (11 * x) - 6

    plt.plot(x, y1, "*", color='yellow', markeredgecolor='k', markersize='7')
    plt.title('Plot of cubic polynomial')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.show()

stars()



def cos_sin():
    x = np.linspace(-2 * np.pi, 2 * np.pi)
    y1 = np.cos(x)
    y2 = np.sin(x)

    plt.figure()
    plt.style.use('bmh')

    plt.subplot(211)
    plt.title('Plot of cos(x) and sin(x)')
    plt.plot(x, y1, label='cos(x)', color='red')
    plt.legend(loc='lower right')
    plt.ylim(-1, 1)
    plt.yticks([-1, 0, 1])
    plt.ylabel('y=cos(x)')

    plt.subplot(212)
    plt.plot(x, y2, label='sin(x)', color='grey')
    plt.legend()
    plt.ylim(-1, 1)
    plt.yticks([-1, 0, 1])
    plt.ylabel('y=sin(x)')
    plt.xlabel('x')

    plt.show()

cos_sin()