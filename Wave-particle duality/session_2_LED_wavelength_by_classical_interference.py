import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt("C:\\Users\\au601136\\Experimental_Quantum_Physics\\Wave-particle duality\\data\\Session 2\\question_2_3.csv", skiprows=1, delimiter=";", dtype=str) 

stage_positions = [float(pos) for pos in [x.replace(",",".") for  x in data[:,0]]]
B_counts = [float(count) for count in [x.replace(",",".") for  x in data[:,7]]] 

def cosine_func(x, A, B, f, φ):
    return A + B*np.cos(2*np.pi*f*x + φ)

popt, pcov = curve_fit(cosine_func, stage_positions, B_counts, p0=[3e6, 3e6, 2.5, 10], maxfev=1000000)

number_of_fringes = popt[2]*10
print("Number of fringes: ", number_of_fringes)

x_fit = np.linspace(stage_positions[0], stage_positions[-1], 10000)
y_fit = cosine_func(x_fit, *popt)

plt.figure(figsize=(10,6))

plt.scatter(stage_positions, B_counts, marker="o", color="firebrick", alpha=0.5, label="Data")
plt.plot(x_fit, y_fit, color="firebrick", label="$\\lambda_{LED} \\approx $%snm" % str(round((2/popt[2]) * 1e3,2)))
plt.xlabel("Stage position [μm]", fontsize=20) 
plt.ylabel("Signal [counts]", fontsize=20)
plt.subplots_adjust(bottom=0.2)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fancybox=True, shadow=True, ncol=4, fontsize=15)
plt.show()