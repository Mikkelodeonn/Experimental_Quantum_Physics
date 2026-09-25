import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt("C:\\Users\\au601136\\Experimental_Quantum_Physics\\Wave-particle duality\\data\\Session 3\\3_2_1.txt", skiprows=1, dtype=str)

angles = [float(angle) for angle in data[:,0]]
rates = [float(x[:-1])*1000 if x.endswith("k") else float(x) for x in [x.replace(",",".") for x in data[:,1]]]

def malus_fit(angle, A, bg):
    T = A*(np.cos(angle*np.pi/180)**2) + bg
    return T

popt, pcov = curve_fit(malus_fit, angles, rates)

xs = np.linspace(angles[0],angles[-1], 10000)
fit_error = np.sqrt(np.diag(pcov))

yfit_upper_error = malus_fit(xs, *(popt+fit_error))
yfit_lower_error = malus_fit(xs, *(popt-fit_error))

plt.figure(figsize=(10,6))
plt.plot(angles, rates, "o", color="firebrick", label="data")
plt.plot(xs, malus_fit(xs, *popt), color="royalblue", label="fit")
plt.fill_between(xs, yfit_lower_error, yfit_upper_error, color="royalblue", alpha=0.3)
plt.xlabel(r"relative polarizer angle [$^\circ$]", fontsize=20)
plt.ylabel("coincidence rate [Hz]", fontsize=20)
#plt.legend(fontsize=20, loc=1)
plt.subplots_adjust(bottom=0.2)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fancybox=True, shadow=True, ncol=3, fontsize=18)
plt.show()