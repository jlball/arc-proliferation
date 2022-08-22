import matplotlib.pyplot as plt
import numpy as np

U_data = np.load("U_data.npy")
Th_data = np.load("Th_data.npy")

percents_fertile = U_data[0] 
fig, ax = plt.subplots()
ax.scatter(percents_fertile, U_data[1]/3600)
ax.scatter(percents_fertile, Th_data[1]/3600)

ax.set_yscale("log")

ax.set_xlabel("Percents Fertile")
ax.set_ylabel("Time to 1 Significant Quantity (hours)")

#plt.show()
plt.savefig("Th_U_time_to_sq")