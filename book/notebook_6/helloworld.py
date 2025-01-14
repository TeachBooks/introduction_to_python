import math
import datetime
import matplotlib.pyplot as plt
import numpy as np

def plot_sine_and_cosine():
    x = np.linspace(0, 2*math.pi, 100)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()
    plt.close()

print("Hello, World!")
print("Today's date is:", datetime.datetime.now())
print("The square root of 16 is:", math.sqrt(16))
print("Here is a (bad) plot of the sin and cos of 0 < x < 2pi:")
plot_sine_and_cosine()