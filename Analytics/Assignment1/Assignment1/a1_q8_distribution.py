import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size = 1000)
plt.hist(x, label="distribution", bins=50)
plt.title("A1_Q8 Distribution Chart")
plt.xlabel("Dataset X")
plt.ylabel("Dataset Y")
plt.legend()
plt.show()