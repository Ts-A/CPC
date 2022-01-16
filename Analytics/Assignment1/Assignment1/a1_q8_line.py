# Line Chart
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
  
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
  
plt.plot(x, y, label="line element")
  
plt.legend()
plt.title("A1_Q8 Line Chart")
plt.xlabel("Dataset X")
plt.ylabel("Dataset Y")
plt.show()