# -*- utf-8 -*-

import random
import statistics
import numpy

numbers = []
for number in range(0, 30):
    random_number = random.randrange(100)
    numbers.append(random_number)

print("Wektor: %s" % numbers)

minimum = min(numbers)
maximum = max(numbers)
print('Minimum: %s' % minimum)
print('Maximum: %s' % maximum)

sorted_numbers = sorted(numbers)
print("Wektor posortowany: %s" % sorted_numbers)

average = numpy.average(numbers)
print('Średnia: %s' % average)

standard_deviation = statistics.stdev(numbers)
print('Odchylenie standardowe: %s' % standard_deviation)

normalized_vector = []
for i in range(0, 30):
    n_v = (numbers[i]-minimum)/(maximum-minimum)
    normalized_vector.append(n_v)

print('Wektor znormalizowany: %s' % normalized_vector)

standardized_vector = []
for i in range(0, 30):
    s_v = (numbers[i]-average)/standard_deviation
    standardized_vector.append(s_v)

print('Wektor standaryzowany: %s' % standardized_vector)




