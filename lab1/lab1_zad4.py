# -*- utf-8 -*-

import random
import numpy as np
import math

vector_one = []
vector_two = []

for i in range(0, 10):
    random_number = random.randrange(20)
    vector_one.append(random_number)

for i in range(0, 10):
    random_number = random.randrange(20)
    vector_two.append(random_number)

print('Wektor pierwszy: %s' % vector_one)
print('Wektor drugi: %s' % vector_two)

print('Iloczyn skalarny: %s' % np.dot(vector_one, vector_two))

vector_one_len = 0
vector_two_len = 0
for i in range(0, 10):
    vector_one_len += vector_one[i]**2
    vector_two_len += vector_two[i]**2

print('Długość wektora pierwszego: %s' % math.sqrt(vector_one_len))
print('Długość wektora drugiego: %s' % math.sqrt(vector_two_len))

cosinus = np.dot(vector_one, vector_two)/(math.sqrt(vector_one_len)*math.sqrt(vector_two_len))
print('cosinus: %s' % cosinus)

angle = math.acos(cosinus)
print('stopnie: %s' % math.degrees(angle))
print('radiany: %s' % angle)