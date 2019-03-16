# -*-utf-8 -*-

import random
import matplotlib as mpl
import numpy as np
import matplotlib.pylab as plt

vector = []

for i in range(0, 101):
    number = random.randrange(21)
    vector.append(number)

numbers = []
for i in range(0, 101):
    numbers.append(i)

vector_count = []
for i in range(0, 21):
    count = 0
    for j in range(len(vector)):
        if vector[j] == i:
            count += 1
    vector_count.append(count)

ypos = np.arange(len(vector_count))

plt.bar(ypos-0.2, vector_count, width=0.4, label='Liczby', color='red')
plt.title('Ilość wystąpień liczb w wektorze')
plt.xticks(ypos, numbers)
plt.xlabel('Liczby')
plt.ylabel('Wystąpienia')
plt.show()

