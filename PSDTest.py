### INITIALIZATION ###
from Fits import *
from CompassLoader import *
from SpectraCalibrator import *
import sys
from matplotlib import rc
rc("text", usetex=True)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['figure.figsize'] = (8, 5)
np.set_printoptions(threshold=sys.maxsize)

# Code used to analyze the first measurements with PSD firmware

### CODE ###
# Data loading
folder = r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PSD_test"
runs = [1,2]                                               # 2 runs
data = np.zeros((2,4095,2))                                # 2 lines (x,y) and 4095 channels
for run in runs:
    data[:, :, run - 1] = CompassLoader(folder + "\HcompassF_run_" + str(run) + "_20220322.root")

# Data calibration
energies = [5156.59, 5485.56, 5804.82]
data_calibrated = data
for run in runs:
    fit, calibrated_x = SpectraCalibrator(data[0,:,run-1], data[1,:,run-1], energies)
    data_calibrated[0,:,run - 1] = calibrated_x

# Data analysis
params = []
R = []
for run in runs:
    fit = Gaussian_fit_spectra(data_calibrated[0,:,run-1], data_calibrated[1,:,run-1], plot=False)
    params.append(fit)
    R.append(fit.get("R[%]"))

# Plot
f, ax = plt.subplots(1, 2, figsize=(16,8))
ax[0].step(data_calibrated[0,:,0], data_calibrated[1,:,0], color="tab:blue")
ax[0].plot(data_calibrated[0,:,0], Gaussian(data_calibrated[0,:,0], params[0].get("amplitude")[0,0], params[0].get("mean")[0,0], params[0].get("sigma")[0,0]), color="tab:red")
ax[0].plot(data_calibrated[0,:,0], Gaussian(data_calibrated[0,:,0], params[0].get("amplitude")[1,0], params[0].get("mean")[1,0], params[0].get("sigma")[1,0]), color="tab:red")
ax[0].plot(data_calibrated[0,:,0], Gaussian(data_calibrated[0,:,0], params[0].get("amplitude")[2,0], params[0].get("mean")[2,0], params[0].get("sigma")[2,0]), color="tab:red")
ax[0].fill_between(data_calibrated[0,:,0], data_calibrated[1,:,0], color="tab:blue", step="pre")
ax[0].text(5200, 11000, str(round(R[0][0][0],2)) + "(" + str(round(R[0][0][1],2)) + ")" + "\%" )
ax[0].text(5500, 11000, str(round(R[0][1][0],2)) + "(" + str(round(R[0][1][1],2)) + ")" + "\%" )
ax[0].text(5820, 5000, str(round(R[0][2][0],2)) + "(" + str(round(R[0][2][1],2)) + ")" + "\%" )
ax[1].step(data_calibrated[0,:,1], data_calibrated[1,:,1], color="tab:blue")
ax[1].plot(data_calibrated[0,:,1], Gaussian(data_calibrated[0,:,1], params[1].get("amplitude")[0,0], params[1].get("mean")[0,0], params[1].get("sigma")[0,0]), color="tab:red")
ax[1].plot(data_calibrated[0,:,1], Gaussian(data_calibrated[0,:,1], params[1].get("amplitude")[1,0], params[1].get("mean")[1,0], params[1].get("sigma")[1,0]), color="tab:red")
ax[1].plot(data_calibrated[0,:,1], Gaussian(data_calibrated[0,:,1], params[1].get("amplitude")[2,0], params[1].get("mean")[2,0], params[1].get("sigma")[2,0]), color="tab:red")
ax[1].fill_between(data_calibrated[0,:,1], data_calibrated[1,:,1], color="tab:blue", step="pre")
ax[1].text(5200, 7000, str(round(R[1][0][0],2)) + "(" + str(round(R[1][0][1],2)) + ")" + "\%" )
ax[1].text(5500, 12000, str(round(R[1][1][0],2)) + "(" + str(round(R[1][1][1],2)) + ")" + "\%" )
ax[1].text(5820, 7000, str(round(R[1][2][0],2)) + "(" + str(round(R[1][2][1],2)) + ")" + "\%" )
ax[0].set_xlim(5000,6000)
ax[1].set_xlim(5000,6000)
ax[0].set_ylim(0)
ax[1].set_ylim(0)
ax[0].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0].set_ylabel("Counts")
ax[0].set_xlabel("Energy (keV)")
ax[1].set_xlabel("Energy (keV)")
ax[0].set_title("CFD fraction = 75\%")
ax[1].set_title("CFD fraction = 50\%")
plt.suptitle("PSD firmware test")
plt.show()