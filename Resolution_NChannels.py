# INITIALIZATION
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(r"C:\Users\Lucas Garrido\Documents\PhD\Codigo\Functions")
from CompassLoader import *
from Spectrum import *
plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = (9, 7)

# DATA LOADING (2 rows (x,y), N bins and 16 channels)
ch07_4096 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\NChannels\HcompassF_Ch07_N4096.root")
ch07_8192 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\NChannels\HcompassF_Ch07_N8192.root")
ch07_16384 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\NChannels\HcompassF_Ch07_N16384.root")
ch815_4096 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\NChannels\HcompassF_Ch815_N4096.root")
ch815_8192 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\NChannels\HcompassF_Ch815_N8192.root")
ch815_16384 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\NChannels\HcompassF_Ch815_N16384.root")

channels = np.arange(16)
energies = [5156, 5485, 5804]       # Pu-239, Am-241 and Cm-244 in keV
data_4096, data_8192, data_16384 = [], [], []
for channel in np.arange(8):
    data_4096.append(Spectrum(ch07_4096[0,:,channel], ch07_4096[1,:,channel]))
    data_8192.append(Spectrum(ch07_8192[0,:,channel], ch07_8192[1,:,channel]))
    data_16384.append(Spectrum(ch07_16384[0,:,channel], ch07_16384[1,:,channel]))
for channel in np.arange(8,16):
    data_4096.append(Spectrum(ch815_4096[0,:,channel], ch815_4096[1,:,channel]))
    data_8192.append(Spectrum(ch815_8192[0,:,channel], ch815_8192[1,:,channel]))
    data_16384.append(Spectrum(ch815_16384[0,:,channel], ch815_16384[1,:,channel]))

fit_4096, fit_8192, fit_16384 = [], [], []
R_Pu_4096, R_Am_4096, R_Cm_4096 = [], [], []
delta_R_Pu_4096, delta_R_Am_4096, delta_R_Cm_4096 = [], [], []
R_Pu_8192, R_Am_8192, R_Cm_8192 = [], [], []
delta_R_Pu_8192, delta_R_Am_8192, delta_R_Cm_8192 = [], [], []
R_Pu_16384, R_Am_16384, R_Cm_16384 = [], [], []
delta_R_Pu_16384, delta_R_Am_16384, delta_R_Cm_16384 = [], [], []
for channel in channels:
    data_4096[channel].calibrate(energies)
    data_8192[channel].calibrate(energies)
    data_16384[channel].calibrate(energies)
    fit_4096.append(data_4096[channel].fit_peaks())
    fit_8192.append(data_8192[channel].fit_peaks())
    fit_16384.append(data_16384[channel].fit_peaks())
    R_Pu_4096.append(fit_4096[channel].get("R[%]")[0][0])
    delta_R_Pu_4096.append(fit_4096[channel].get("R[%]")[0][1])
    R_Am_4096.append(fit_4096[channel].get("R[%]")[1][0])
    delta_R_Am_4096.append(fit_4096[channel].get("R[%]")[1][1])
    R_Cm_4096.append(fit_4096[channel].get("R[%]")[2][0])
    delta_R_Cm_4096.append(fit_4096[channel].get("R[%]")[2][1])
    R_Pu_8192.append(fit_8192[channel].get("R[%]")[0][0])
    delta_R_Pu_8192.append(fit_8192[channel].get("R[%]")[0][1])
    R_Am_8192.append(fit_8192[channel].get("R[%]")[1][0])
    delta_R_Am_8192.append(fit_8192[channel].get("R[%]")[1][1])
    R_Cm_8192.append(fit_8192[channel].get("R[%]")[2][0])
    delta_R_Cm_8192.append(fit_8192[channel].get("R[%]")[2][1])
    R_Pu_16384.append(fit_16384[channel].get("R[%]")[0][0])
    delta_R_Pu_16384.append(fit_16384[channel].get("R[%]")[0][1])
    R_Am_16384.append(fit_16384[channel].get("R[%]")[1][0])
    delta_R_Am_16384.append(fit_16384[channel].get("R[%]")[1][1])
    R_Cm_16384.append(fit_16384[channel].get("R[%]")[2][0])
    delta_R_Cm_16384.append(fit_16384[channel].get("R[%]")[2][1])

channels = channels + 1
f, ax = plt.subplots(1, 3, figsize=(19,7))
ax[0].bar(channels - 0.25, R_Pu_4096, yerr=delta_R_Pu_4096, color="tab:red", width=0.2, align="center", label="Pu-239", capsize=3)
ax[0].bar(channels, R_Am_4096, yerr=delta_R_Am_4096, color="tab:purple", width=0.2, align="center", label="Am-241", capsize=3)
ax[0].bar(channels + 0.25, R_Cm_4096, yerr=delta_R_Cm_4096, color="tab:cyan", width=0.2, align="center", label="Cm-244", capsize=3)
ax[0].set_xticks(channels)
ax[0].set_xlabel("Channels")
ax[0].set_ylabel("Resolution [\%]")
ax[0].set_title("4096")
ax[0].set_ylim(0.1,0.25)
ax[0].legend()

ax[1].bar(channels - 0.25, R_Pu_8192, yerr=delta_R_Pu_8192, color="tab:red", width=0.2, align="center", label="Pu-239", capsize=3)
ax[1].bar(channels, R_Am_8192, yerr=delta_R_Am_8192, color="tab:purple", width=0.2, align="center", label="Am-241", capsize=3)
ax[1].bar(channels + 0.25, R_Cm_8192, yerr=delta_R_Cm_8192, color="tab:cyan", width=0.2, align="center", label="Cm-244", capsize=3)
ax[1].set_xticks(channels)
ax[1].set_xlabel("Channels")
ax[1].set_title("8192")
ax[1].set_ylim(0.1,0.25)
ax[1].legend()

ax[2].bar(channels - 0.25, R_Pu_16384, yerr=delta_R_Pu_16384, color="tab:red", width=0.2, align="center", label="Pu-239", capsize=3)
ax[2].bar(channels, R_Am_16384, yerr=delta_R_Am_16384, color="tab:purple", width=0.2, align="center", label="Am-241", capsize=3)
ax[2].bar(channels + 0.25, R_Cm_16384, yerr=delta_R_Cm_16384, color="tab:cyan", width=0.2, align="center", label="Cm-244", capsize=3)
ax[2].set_xticks(channels)
ax[2].set_xlabel("Channels")
ax[2].set_title("16384")
ax[2].set_ylim(0.1,0.25)
plt.legend()
plt.tight_layout()
plt.show()

# k = 10
# data_4096[k].plot_fit(xlim=(5000,6000))
# plt.show()
# data_8192[k].plot_fit(xlim=(5000,6000))
# plt.show()
# data_16384[k].plot_fit(xlim=(5000,6000))
# plt.show()

R_4096 = R_Am_4096 + R_Pu_4096 + R_Cm_4096
R_8192 = R_Am_8192 + R_Pu_8192 + R_Cm_8192
R_16384 = R_Am_16384 + R_Pu_16384 + R_Cm_16384
R_err_4096 = delta_R_Cm_4096 + delta_R_Pu_4096 + delta_R_Am_4096
R_err_8192 = delta_R_Cm_8192 + delta_R_Pu_8192 + delta_R_Am_8192
R_err_16384 = delta_R_Cm_16384 + delta_R_Pu_16384 + delta_R_Am_16384
mean_4096 = sum(R_4096)/len(R_4096)
mean_8192 = sum(R_8192)/len(R_8192)
mean_16384 = sum(R_16384)/len(R_16384)
std_4096 = np.sqrt(sum([(x-mean_4096)**2 for x in R_4096])/len(R_4096))
std_8192 = np.sqrt(sum([(x-mean_8192)**2 for x in R_8192])/len(R_8192))
std_16384 = np.sqrt(sum([(x-mean_16384)**2 for x in R_16384])/len(R_16384))
mean_err_4096 = sum(R_err_4096)/len(R_err_4096)
mean_err_8192 = sum(R_err_8192)/len(R_err_8192)
mean_err_16384 = sum(R_err_16384)/len(R_err_16384)

print("N = 4096 -->", "R_mean:", mean_4096, "R_err_mean:", mean_err_4096, "R_std:", std_4096)
print("N = 8192 -->", "R_mean:", mean_8192, "R_err_mean:", mean_err_8192, "R_std:", std_8192)
print("N = 16384 -->", "R_mean:", mean_16384, "R_err_mean:", mean_err_16384, "R_std:", std_16384)
