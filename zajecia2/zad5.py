from pylab import *
 
x = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9]
y = [10,9,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2]
 
x_a = arange(len(x)) 
 
ax = subplot(111)
bar(x_a, y)
xticks( x_a + 0.5,x )
show()