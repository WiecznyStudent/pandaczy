import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,8), dpi=100)

x=np.arange(-10,10,0.1)
y=x**2

plt.xlabel('oś x')
plt.ylabel('oś y')
plt.axhline(y=0, color="#cccccc")
plt.axvline(x=0, color="#cccccc")
plt.title('wykres y=x^2')

plt.plot(x,y)
plt.show()