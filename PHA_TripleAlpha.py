# INITIALIZATION
import sys

import matplotlib.pyplot as plt

sys.path.append(r"C:\Users\Lucas Garrido\Documents\PhD\Codigo\Functions")
from CompassLoader import *
from Spectrum import *

# DATA LOADING, CALIBRATION AND FITTING
channels = np.arange(16)
file = uproot.open(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\SDataF_run_TripleAlpha.root")
events = file["Data_F"]["Channel"].array()
plt.hist(events, bins=16, rwidth=1, align="left")
plt.xticks(channels)
plt.ylim(450000,450150)
plt.xlabel("Channel")
plt.ylabel("Counts")
plt.title("\# of events")
plt.show()

data = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_run_TripleAlpha.root")
spectra = []
energies = [5156, 5485, 5804]                                         # Pu-239, Am-241 and Cm-244 in keV
for channel in channels:
    spectra.append(Spectrum(data[0,:,channel], data[1,:,channel]))    # the 16 spectra of the 16 channels

R_Pu = []
R_Am = []
R_Cm = []
delta_R_Pu = []
delta_R_Am = []
delta_R_Cm = []
for channel in channels:
    spectra[channel].calibrate(energies)                              # calibrates every channel
    # spectra[channel].plot(xlim=(5000,6000))                           # plot
    fit = spectra[channel].fit_peaks()                                # fitting
    R_Pu.append(fit.get("R[%]")[0][0])
    delta_R_Pu.append(fit.get("R[%]")[0][1])
    R_Am.append(fit.get("R[%]")[1][0])
    delta_R_Am.append(fit.get("R[%]")[1][1])
    R_Cm.append(fit.get("R[%]")[2][0])
    delta_R_Cm.append(fit.get("R[%]")[2][1])

plt.bar(channels - 0.25, R_Pu, yerr=delta_R_Pu, color="tab:red", width=0.2, align="center", label="Pu-239", capsize=3)
plt.bar(channels, R_Am, yerr=delta_R_Am, color="tab:purple", width=0.2, align="center", label="Am-241", capsize=3)
plt.bar(channels + 0.25, R_Cm, yerr=delta_R_Cm, color="tab:cyan", width=0.2, align="center", label="Cm-244", capsize=3)
plt.legend()
plt.xticks(channels)
plt.xlabel("Channels")
plt.ylabel("Resolution [\%]")
plt.title("Triple alpha")
plt.show()

