import matplotlib.pyplot as plt
x = [-10,10]
a = float(input('Podaj A: '))
b = float(input('Podaj B: '))
c = a*x[0]+b
d = a*x[1]+b
y=[c,d]
plt.plot(a,b,y)
plt.show()