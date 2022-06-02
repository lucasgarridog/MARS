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
ch07_1 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\FineGain\HcompassF_Ch07_G1.root")
ch07_2 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\FineGain\HcompassF_Ch07_G2.root")
ch07_3 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\FineGain\HcompassF_Ch07_G3.root")
ch815_1 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\FineGain\HcompassF_Ch815_G1.root")
ch815_2 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\FineGain\HcompassF_Ch815_G2.root")
ch815_3 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\FineGain\HcompassF_Ch815_G3.root")

channels = np.arange(16)
energies = [5156, 5485, 5804]       # Pu-239, Am-241 and Cm-244 in keV
data_1, data_2, data_3 = [], [], []
for channel in np.arange(8):
    data_1.append(Spectrum(ch07_1[0,:,channel], ch07_1[1,:,channel]))
    data_2.append(Spectrum(ch07_2[0,:,channel], ch07_2[1,:,channel]))
    data_3.append(Spectrum(ch07_3[0,:,channel], ch07_3[1,:,channel]))
for channel in np.arange(8,16):
    data_1.append(Spectrum(ch815_1[0,:,channel], ch815_1[1,:,channel]))
    data_2.append(Spectrum(ch815_2[0,:,channel], ch815_2[1,:,channel]))
    data_3.append(Spectrum(ch815_3[0,:,channel], ch815_3[1,:,channel]))

fit_1, fit_2, fit_3 = [], [], []
R_Pu_1, R_Am_1, R_Cm_1 = [], [], []
delta_R_Pu_1, delta_R_Am_1, delta_R_Cm_1 = [], [], []
R_Pu_2, R_Am_2, R_Cm_2 = [], [], []
delta_R_Pu_2, delta_R_Am_2, delta_R_Cm_2 = [], [], []
R_Pu_3, R_Am_3, R_Cm_3 = [], [], []
delta_R_Pu_3, delta_R_Am_3, delta_R_Cm_3 = [], [], []
for channel in channels:
    data_1[channel].calibrate(energies)
    data_2[channel].calibrate(energies)
    data_3[channel].calibrate(energies)
    fit_1.append(data_1[channel].fit_peaks())
    fit_2.append(data_2[channel].fit_peaks())
    fit_3.append(data_3[channel].fit_peaks())
    R_Pu_1.append(fit_1[channel].get("R[%]")[0][0])
    delta_R_Pu_1.append(fit_1[channel].get("R[%]")[0][1])
    R_Am_1.append(fit_1[channel].get("R[%]")[1][0])
    delta_R_Am_1.append(fit_1[channel].get("R[%]")[1][1])
    R_Cm_1.append(fit_1[channel].get("R[%]")[2][0])
    delta_R_Cm_1.append(fit_1[channel].get("R[%]")[2][1])
    R_Pu_2.append(fit_2[channel].get("R[%]")[0][0])
    delta_R_Pu_2.append(fit_2[channel].get("R[%]")[0][1])
    R_Am_2.append(fit_2[channel].get("R[%]")[1][0])
    delta_R_Am_2.append(fit_2[channel].get("R[%]")[1][1])
    R_Cm_2.append(fit_2[channel].get("R[%]")[2][0])
    delta_R_Cm_2.append(fit_2[channel].get("R[%]")[2][1])
    R_Pu_3.append(fit_3[channel].get("R[%]")[0][0])
    delta_R_Pu_3.append(fit_3[channel].get("R[%]")[0][1])
    R_Am_3.append(fit_3[channel].get("R[%]")[1][0])
    delta_R_Am_3.append(fit_3[channel].get("R[%]")[1][1])
    R_Cm_3.append(fit_3[channel].get("R[%]")[2][0])
    delta_R_Cm_3.append(fit_3[channel].get("R[%]")[2][1])

channels = channels + 1
f, ax = plt.subplots(1, 3, figsize=(19,7))
ax[0].bar(channels - 0.25, R_Pu_1, yerr=delta_R_Pu_1, color="tab:red", width=0.2, align="center", label="Pu-239", capsize=3)
ax[0].bar(channels, R_Am_1, yerr=delta_R_Am_1, color="tab:purple", width=0.2, align="center", label="Am-241", capsize=3)
ax[0].bar(channels + 0.25, R_Cm_1, yerr=delta_R_Cm_1, color="tab:cyan", width=0.2, align="center", label="Cm-244", capsize=3)
ax[0].set_xticks(channels)
ax[0].set_xlabel("Channels")
ax[0].set_ylabel("Resolution [\%]")
ax[0].set_title("1")
ax[0].set_ylim(0.1,0.16)
ax[0].legend(loc="lower left", framealpha=1)

ax[1].bar(channels - 0.25, R_Pu_2, yerr=delta_R_Pu_2, color="tab:red", width=0.2, align="center", label="Pu-239", capsize=3)
ax[1].bar(channels, R_Am_2, yerr=delta_R_Am_2, color="tab:purple", width=0.2, align="center", label="Am-241", capsize=3)
ax[1].bar(channels + 0.25, R_Cm_2, yerr=delta_R_Cm_2, color="tab:cyan", width=0.2, align="center", label="Cm-244", capsize=3)
ax[1].set_xticks(channels)
ax[1].set_xlabel("Channels")
ax[1].set_title("2")
ax[1].set_ylim(0.1,0.16)
ax[1].legend(loc="lower left", framealpha=1)

ax[2].bar(channels - 0.25, R_Pu_3, yerr=delta_R_Pu_3, color="tab:red", width=0.2, align="center", label="Pu-239", capsize=3)
ax[2].bar(channels, R_Am_3, yerr=delta_R_Am_3, color="tab:purple", width=0.2, align="center", label="Am-241", capsize=3)
ax[2].bar(channels + 0.25, R_Cm_3, yerr=delta_R_Cm_3, color="tab:cyan", width=0.2, align="center", label="Cm-244", capsize=3)
ax[2].set_xticks(channels)
ax[2].set_xlabel("Channels")
ax[2].set_title("3")
ax[2].set_ylim(0.1,0.16)
ax[2].legend(loc="lower left", framealpha=1)
plt.tight_layout()
plt.show()

# k = 0
# plt.figure(1)
# data_1[k].plot(xlim=(5000,6000))
# plt.figure(2)
# data_2[k].plot(xlim=(5000,6000))
# plt.figure(3)
# data_3[k].plot(xlim=(5000,6000))
# plt.show()

R_1 = R_Am_1 + R_Pu_1 + R_Cm_1
R_2 = R_Am_2 + R_Pu_2 + R_Cm_2
R_3 = R_Am_3 + R_Pu_3 + R_Cm_3
R_err_1 = delta_R_Cm_1 + delta_R_Pu_1 + delta_R_Am_1
R_err_2 = delta_R_Cm_2 + delta_R_Pu_2 + delta_R_Am_2
R_err_3 = delta_R_Cm_3 + delta_R_Pu_3 + delta_R_Am_3
mean_1 = sum(R_1)/len(R_1)
mean_2 = sum(R_2)/len(R_2)
mean_3 = sum(R_3)/len(R_3)
std_1 = np.sqrt(sum([(x-mean_1)**2 for x in R_1])/len(R_1))
std_2 = np.sqrt(sum([(x-mean_2)**2 for x in R_2])/len(R_2))
std_3 = np.sqrt(sum([(x-mean_3)**2 for x in R_3])/len(R_3))
mean_err_1 = sum(R_err_1)/len(R_err_1)
mean_err_2 = sum(R_err_2)/len(R_err_2)
mean_err_3 = sum(R_err_3)/len(R_err_3)

print("G = 1 -->", "R_mean:", mean_1, "R_err_mean:", mean_err_1, "R_std:", std_1)
print("G = 2 -->", "R_mean:", mean_2, "R_err_mean:", mean_err_2, "R_std:", std_2)
print("G = 3 -->", "R_mean:", mean_3, "R_err_mean:", mean_err_3, "R_std:", std_3)
