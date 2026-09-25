import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

angles = np.arange(0,360,10)
power = [0.335, 0.333, 0.301, 0.27, 0.21, 0.16, 0.1, 0.05, 0.02, 0.01, 0.015, 0.038, 0.081, 0.136, 0.190, 0.250, 0.289, 0.322, 0.334, 0.339, 0.299, 0.260, 0.208, 0.156, 0.102, 0.058, 0.025, 0.009, 0.012, 0.035, 0.072, 0.117, 0.181, 0.242, 0.277, 0.319]
power_error = [0.01] * len(power)
angles_error = [1] * len(angles)

def malus_fit(angle, A, bg):
    T = A*(np.cos(angle*np.pi/180)**2) + bg
    return T

popt, pcov = curve_fit(malus_fit, angles, power)

xs = np.linspace(0,350, 10000)
fit_error = np.sqrt(np.diag(pcov))

yfit_upper_error = malus_fit(xs, *(popt+fit_error))
yfit_lower_error = malus_fit(xs, *(popt-fit_error))

plt.figure(figsize=(10,6))
plt.errorbar(angles, power, yerr=power_error, xerr=angles_error, fmt=".", capsize=3, color="firebrick", label="data")
plt.plot(xs, malus_fit(xs, *popt), color="royalblue", label="fit")
plt.fill_between(xs, yfit_lower_error, yfit_upper_error, color="royalblue", alpha=0.3)
plt.xlabel(r"relative polarizer angle [$^\circ$]", fontsize=20)
plt.ylabel("power [mW]", fontsize=20)
#plt.legend(fontsize=20, loc=1)
plt.subplots_adjust(bottom=0.2)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fancybox=True, shadow=True, ncol=3, fontsize=18)
plt.show()