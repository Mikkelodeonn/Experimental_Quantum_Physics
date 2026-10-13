import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt("C:\\Users\\au601136\\Experimental_Quantum_Physics\\Wave-particle duality\\data\\Session 2\\question_2_1_1.csv", skiprows=1, delimiter=";", dtype=str) 

delay_times = [float(delay) for delay in [x.replace(",",".") for  x in data[:,0]]]
TA_rates = [float(rate) for rate in [x.replace(",",".") for  x in data[:,1]]]
TB_rates = [float(rate) for rate in [x.replace(",",".") for  x in data[:,2]]]

def gaussian(x, A, σ, x0, B):
    g = A * np.exp(-(x-x0)**2 / (2*σ**2)) + B
    return g

TA_popt, TA_pcov = curve_fit(gaussian, delay_times, TA_rates)
TB_popt, TB_pcov = curve_fit(gaussian, delay_times, TB_rates)

TA_optimal_delay_time = TA_popt[2]
TB_optimal_delay_time = TB_popt[2]

delay_times_fit = np.linspace(delay_times[0], delay_times[-1], 10000)
TA_rates_fit = gaussian(delay_times_fit, *TA_popt)
TB_rates_fit = gaussian(delay_times_fit, *TB_popt)

plt.figure(figsize=(10,6))

plt.scatter(delay_times, TA_rates, marker="o", color="firebrick", alpha=0.5, label="T&A")
plt.scatter(delay_times, TB_rates, marker="o", color="royalblue", alpha=0.5, label="T&B")
plt.plot(delay_times_fit, TA_rates_fit, color="firebrick", label="$\\Delta t^{T&A}_{opt} = $%sns" % str(round(TA_optimal_delay_time,2)))
plt.plot(delay_times_fit, TB_rates_fit, color="royalblue", label="$\\Delta t^{T&B}_{opt} = $%sns" % str(round(TB_optimal_delay_time,2)))
plt.xlabel("Delay between detectors A/B and T [ns]", fontsize=20)
plt.ylabel("Coincidence rate [Hz]", fontsize=20)
plt.subplots_adjust(bottom=0.2)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fancybox=True, shadow=True, ncol=4, fontsize=15)
plt.show()