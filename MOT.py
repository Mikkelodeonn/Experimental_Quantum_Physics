import numpy as np
import matplotlib.pyplot as plt

doppler_free_data = np.loadtxt(r"C:\Users\au601136\Experimental_Quantum_Physics\data\session 1\doppler_free_peaks2.csv", delimiter=",", skiprows=1, usecols=(0,1,2))
doppler_full_data = np.loadtxt(r"C:\Users\au601136\Experimental_Quantum_Physics\data\session 1\doppler_full_peaks2.csv", delimiter=",", skiprows=1, usecols=(0,1,2))


# channel 1 -> triangular signal (frequency and power)
# channel 2 -> signal
# channel 4 -> square

fig, ax = plt.subplots()

ax.plot(doppler_free_data[:,1] - doppler_full_data[:,1])
plt.show()