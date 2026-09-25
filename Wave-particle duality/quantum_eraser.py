import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data1 = np.loadtxt("C:\\Users\\au601136\\Experimental_Quantum_Physics\\Wave-particle duality\\data\\Session 3\\3_3_2.csv", skiprows=1, delimiter=";", dtype=str)
data2 = np.loadtxt("C:\\Users\\au601136\\Experimental_Quantum_Physics\\Wave-particle duality\\data\\Session 3\\3_3_3.csv", skiprows=1, delimiter=";", dtype=str)
data3 = np.loadtxt("C:\\Users\\au601136\\Experimental_Quantum_Physics\\Wave-particle duality\\data\\Session 3\\3_3_4.csv", skiprows=1, delimiter=";", dtype=str)


stage_positions1 = [float(pos) for pos in [x.replace(",",".") for  x in data1[:,0]]][:121]
rates1 = [float(rate) for rate in [x.replace(",",".") for x in data1[:,1]]][:121]
g2s1 = [float(g2) for g2 in [x.replace(",",".") for x in data1[:,3]]][:121]

stage_positions2 =  [float(pos) for pos in [x.replace(",",".") for  x in data2[:,0]]]
rates2 = [ float(x) for x in [x.replace(",",".") for x in data2[:,1]]]
g2s2 = [float(g2) for g2 in [x.replace(",",".") for x in data2[:,3]]]

stage_positions3 =  [float(pos) for pos in [x.replace(",",".") for  x in data3[:,0]]]
rates3 = [float(x) for x in [x.replace(",",".") for x in data3[:,1]]]
g2s3 = [float(g2) for g2 in [x.replace(",",".") for x in data3[:,3]]]

print(len(stage_positions1), len(stage_positions2), len(stage_positions3))

plt.figure(figsize=(10,6))

#plt.plot(stage_positions1, rates1, "o", color="firebrick", label=r"$0^{\circ} / 0^{\circ}$")
#plt.plot(stage_positions2, rates2, "o", color="royalblue", label=r"$90^{\circ} / 0^{\circ}$")
#plt.plot(stage_positions3, rates3, "o", color="forestgreen", label=r"$90^{\circ} / 0^{\circ} / 45^{\circ}$")

plt.plot(stage_positions1, g2s1, "o", color="firebrick", label=r"$0^{\circ} / 0^{\circ}$")
plt.plot(stage_positions2, g2s2, "o", color="royalblue", label=r"$90^{\circ} / 0^{\circ}$")
plt.plot(stage_positions3, g2s3, "o", color="forestgreen", label=r"$90^{\circ} / 0^{\circ} / 45^{\circ}$")

plt.xlabel("stage position [μm]", fontsize=20) 
#plt.ylabel("coincidence rate [Hz]", fontsize=20)
plt.ylabel(r"$g^{(2)}(0)$", fontsize=20)
#plt.legend(fontsize=20, loc=1)
plt.subplots_adjust(bottom=0.2)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fancybox=True, shadow=True, ncol=3, fontsize=18)
plt.show()