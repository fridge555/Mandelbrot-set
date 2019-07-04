from math import sqrt
import numpy as mp
import matplotlib.pyplot as plt


def mod(complex_no):
    num = sqrt(complex_no.real ** 2 + complex_no.imag ** 2)
    return num

def div_check(complex_no):
    n = 0
    d = 0
    while n < 100:
        d = d ** 2 + complex_no
        if mod(d) > 2 and n < 10:
            return 'red'
        elif mod(d) > 2 and n < 20:
            return 'orange'
        elif mod(d) > 2 and n < 30:
            return 'yellow'
        elif mod(d) > 2 and n < 100:
            return 'blank'
        n += 1
    return 'convergent'

dict = {
    }

x_list = []
y_list = []

for x in range(-100,101):
    x_list.append(x / 50)
    y_list.append((x / 50))

for x in x_list:
    for y in y_list:
        dict[x , y] = div_check(x + y*1j)
        if dict[x , y] == 'convergent':
            plt.scatter(x , y , color = 'black')
        elif dict[x , y] == 'blank':
            pass
        else:
            plt.scatter(x , y , color = '%s' % dict[x , y])

plt.show()
