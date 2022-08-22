import matplotlib.pyplot as plt
import numpy as np

U_data = np.load("U_data.npy")
Th_data = np.load("Th_data.npy")

times = U_data[0]

fig, ax = plt.subplots()
ax.scatter(times, U_data[1])
ax.scatter(times, Th_data[1])

ax.set_yscale("log")

ax.set_xlabel("Percents Fertile")
ax.set_ylabel("Time to 1 Significant Quantity")

plt.show()