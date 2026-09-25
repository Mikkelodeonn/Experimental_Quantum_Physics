import numpy as np
import matplotlib.pyplot as plt

def photon_num_dist(n, n_mean):
    P = (n_mean**n) / ((1 + n_mean)**(n+1))
    return P

photon_numbers = np.arange(0,24)
photon_mean = 5

P = photon_num_dist(photon_numbers, photon_mean)
print(np.sum(P))

plt.figure(figsize=(10,6))
plt.bar(photon_numbers, P, width=0.8, label="$\\langle n \\rangle = 5 $")
plt.xlabel("photon number", fontsize=24)
plt.ylabel("probability", fontsize=24)
plt.legend(fontsize=20)
plt.show()