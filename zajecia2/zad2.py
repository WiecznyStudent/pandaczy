import pylab

x = pylab.arange(-10, 10, 0.5) 
a = int(input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]

y2 = [i**2 / 3 for i in x if i >= 0]

pylab.plot(x[:len(y1)], y1, x[-len(y2):], y2)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()
