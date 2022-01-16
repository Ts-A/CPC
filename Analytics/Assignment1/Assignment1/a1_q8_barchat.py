# plot bar on a randomly generated values
import numpy as np
import matplotlib.pyplot as plt

x = list(np.random.randint(low=1, high=100, size=50))

y = list(np.random.randint(low=1, high=100, size=50))

fig = plt.figure(figsize=(10, 5))

plt.bar(x, y, color='red', label="barchart", width=0.4)

plt.xlabel("Dataset X")
plt.ylabel("Dataset Y")
plt.title("A1-Q8 Bar Chart")
plt.legend()
plt.show()
