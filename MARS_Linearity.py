# INITIALIZATION
import sys
import numpy as np
sys.path.append(r"C:\Users\Lucas Garrido\Documents\PhD\Codigo\Functions")
from CompassLoader import *
from Spectrum import *
from tabulate import tabulate
import matplotlib.patches as patches
plt.rcParams['font.size'] = 22
plt.rcParams['figure.figsize'] = (9, 7)

# DATA LOADING (2 rows (x,y), N bins and 16 channels)
# PHA_raw_data = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\Linearity\HcompassF_run_PHALinearity.root")
PHA_raw_data_1 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\Linearity\HcompassF_single1_PHA.root")
# PHA_raw_data_1 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\Linearity\HcompassF_single2_test.root")
PHA_raw_data_2 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\Linearity\HcompassF_single2_PHA.root")
# PHA_raw_data_2 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\Linearity\HcompassF_single1_test.root")
channels = np.arange(16)
v_in = np.array([0.26, 0.52, 0.78, 1.06, 1.31, 1.56])
PHA_data = []
for channel in np.arange(8):
    PHA_data.append(Spectrum(PHA_raw_data_1[0,:,channel], PHA_raw_data_1[1,:,channel]))

for channel in np.arange(8,16):
    PHA_data.append(Spectrum(PHA_raw_data_2[0,:,channel], PHA_raw_data_2[1,:,channel]))

PHA_linear_fits = []
for channel in channels:
    peaks = PHA_data[channel].peaks()
    fit = Linear_fit(v_in, peaks)
    M = fit.get("slope")
    M_err = fit.get("delta_slope")
    N = fit.get("intercept")
    N_err = fit.get("delta_intercept")
    r_2 = fit.get("r_squared")
    PHA_linear_fits.append([M, M_err, N, N_err])
    fig = plt.figure(1)
    plt.plot(v_in, peaks, "kx", zorder=1)
    x = np.linspace(v_in[0], v_in[-1])
    plt.plot(x, Linear(x, M, N), "r--", zorder=0, label="Channel " + str(channel))
    plt.xlabel("Input height (V)")
    plt.ylabel("Channel")
    # plt.legend()
    text = "m = " + "%.0f" % M + " $\pm$ " + "%.0f" % M_err + "\n" + "n = " + "%.0f" % N + " $\pm$ " + "%.0f" % N_err + "\n" + "$r^2$ = " + "%.4f" % r_2
    plt.text(0.15, 0.74, text, transform=fig.transFigure, bbox=dict(facecolor="white"))
    plt.show()
table_indexes = ["Channel 0", "Channel 1", "Channel 2", "Channel 3", "Channel 4", "Channel 5", "Channel 6", "Channel 7", "Channel 8", "Channel 9", "Channel 10", "Channel 11", "Channel 12", "Channel 13", "Channel 14", "Channel 15"]
table_headers = ["Slope", "d_Slope", "Intercept", "d_Intercept"]
print(tabulate(PHA_linear_fits, headers=table_headers, showindex=table_indexes, floatfmt=".0f"))

fit = PHA_data[0].fit_peaks()
A, MU, SIGMA = fit.get("amplitude")[1,0], fit.get("mean")[1,0], fit.get("sigma")[1,0]
x = np.linspace(PHA_raw_data_1[0,4660,0],PHA_raw_data_1[0,4680,0])
PHA_data[0].plot()
plt.gca().add_patch(patches.Rectangle((4270,0),800,1650,linewidth=1,linestyle="--",edgecolor="black",facecolor='none'))
plt.xlim(0,16383)
plt.ylim(0,3000)
plt.plot([4270,9000], [1650,2880], color="black", linewidth=1, zorder=0, linestyle="--")
plt.plot([4270+800,15300], [0,1710], color="black", linewidth=1, zorder=0, linestyle="--")
plt.title("")
ax2 = plt.axes([.55, .55, .3, .3])
ax2.step(PHA_raw_data_1[0,4660:4680,0], PHA_raw_data_1[1,4660:4680,0], color="tab:blue", where="mid")
ax2.fill_between(PHA_raw_data_1[0,4660:4680,0], PHA_raw_data_1[1,4660:4680,0], color="tab:blue", step="mid")
ax2.plot(x, Gaussian(x,A,MU,SIGMA), color="tab:red")
ax2.set_ylim(0)
plt.setp(ax2, xticks=[], yticks=[])
plt.show()

FWHMs = []
Rs = []
delta_FWHMs = []
delta_Rs = []
for channel in channels:
    fit = PHA_data[channel].fit_peaks()
    FWHMs.append(fit.get("FWHM")[:,0])
    Rs.append(fit.get("R[%]")[:,0])
    delta_Rs.append(fit.get("R[%]")[:,1])
    delta_FWHMs.append(fit.get("FWHM")[:,1])

k = 8
plt.figure()
PHA_data[k].plot_fit()
plt.show()
print(tabulate(FWHMs, showindex=table_indexes, floatfmt=".2f"))
print(tabulate(delta_FWHMs, showindex=table_indexes, floatfmt=".2f"))

# print(tabulate(Rs, headers=table_headers, showindex=table_indexes, floatfmt=".3f"))
# print(tabulate(delta_Rs, headers=table_headers, showindex=table_indexes, floatfmt=".3f"))
