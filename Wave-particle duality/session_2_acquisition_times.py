import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


acquisition_times = ["0_001ms", "0_010ms", "0_100ms", "1ms", "10ms", "100ms", "1000ms"]
time_labels = ["0.001ms", "0.01ms", "0.1ms", "1ms", "10ms", "100ms", "1000ms"]

datas = [np.loadtxt("C:\\Users\\au601136\\Experimental_Quantum_Physics\\Wave-particle duality\\data\\Session 2\\question_2_5_"+time+".csv", skiprows=1, delimiter=";", dtype=str) for time in acquisition_times] 

xdatas = []
ydatas = []

for data in datas:
    stage_positions =  [float(pos) for pos in [x.replace(",",".") for  x in data[:,0]]]
    rates = [float(x) for x in [x.replace(",",".") for x in data[:,1]]]

    xdatas.append(stage_positions)
    ydatas.append(rates)

fig, ax = plt.subplots(nrows=7 , ncols=1, figsize=(12,18))

for i in range(7):
    ax[i].plot(xdatas[i], ydatas[i], color="royalblue", label=time_labels[i])
    ax[i].ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))

    if i in range(6): 
        ax[i].set_xticklabels([])
    else: 
        pass

    ax[i].legend(loc="upper right", fontsize=15)
    ax[i].grid(alpha=0.5)

fig.supylabel("coincidence rates [arb. u.]", fontsize=20)
fig.supxlabel("stage position [μm]", fontsize=20)

plt.show()

