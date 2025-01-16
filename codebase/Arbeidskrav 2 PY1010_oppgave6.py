"""
Program : PY1010 Arbeidskrav 2  (Oppg 6)
Created on Thu Jan 16 2025
Author : Ghanashyam Niroula
"""
import numpy as np
import matplotlib.pyplot as plt

# Definer funksjonen f(x) = -x^2 - 5
def f(x):
    return -x**2 - 5

# Generer x-verdier i intervallet [-10, 10]
x = np.linspace(-10, 10, 400)
# Beregn y-verdiene for de genererte x-verdiene
y = f(x)

# Plotter funksjonen
plt.plot(x, y, label=r"$f(x) = -x^2 - 5$")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot av funksjonen f(x) = -x^2 - 5')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
