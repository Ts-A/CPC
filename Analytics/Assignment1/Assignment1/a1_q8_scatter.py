# scatter plot on a randomly generated set of values
import matplotlib.pyplot as plt
import numpy as np

x = list(np.random.randint(low=1, high=100, size=50))

y = list(np.random.randint(low=1, high=100, size=50))

plt.scatter(x, y, label="scatter", c="red")

plt.xlabel("Dataset-X")
plt.ylabel("Dataset-Y")
plt.title("A1-Q8 Scatter Plot")
plt.legend()

plt.show()
