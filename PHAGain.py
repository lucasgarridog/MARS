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

# Code used to study the resolution dependence on the gain

### CODE ###
# Data loading
folder = r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA_test\Gain"
runs = [1,2,3]
data = np.zeros((2,4095,3))
for run in runs:
    data[:,:,run-1] = CompassLoader(folder + "\HCompassF_run_" + str(run) + "_20220328.root")

# Data calibration
energies = [5156.59, 5485.56, 5804.82]
data_calibrated = data
for run in runs:
    cal_fit, calibrated_x = SpectraCalibrator(data[0,:,run-1], data[1,:,run-1], energies)
    data_calibrated[0,:,run-1] = calibrated_x

# Data analysis
params = []
R = []
for run in runs:
    fit = Gaussian_fit_spectra(data_calibrated[0,:,run-1], data_calibrated[1,:,run-1], plot=False)
    params.append(fit)
    R.append(fit.get("R[%]"))

# Plot
new_x = np.linspace(5000,6000,1000)
f, ax = plt.subplots(1, 3, figsize=(16,8))
ax[0].step(data_calibrated[0,:,0], data_calibrated[1,:,0], color="tab:blue")
ax[0].fill_between(data_calibrated[0,:,0], data_calibrated[1,:,0], color="tab:blue", step="pre")
ax[1].step(data_calibrated[0,:,1], data_calibrated[1,:,1], color="tab:blue")
ax[1].fill_between(data_calibrated[0,:,1], data_calibrated[1,:,1], color="tab:blue", step="pre")
ax[2].step(data_calibrated[0,:,2], data_calibrated[1,:,2], color="tab:blue")
ax[2].fill_between(data_calibrated[0,:,2], data_calibrated[1,:,2], color="tab:blue", step="pre")
ax[0].plot(new_x, Gaussian(new_x, params[0].get("amplitude")[0,0], params[0].get("mean")[0,0], params[0].get("sigma")[0,0]), color="tab:red")
ax[0].plot(new_x, Gaussian(new_x, params[0].get("amplitude")[1,0], params[0].get("mean")[1,0], params[0].get("sigma")[1,0]), color="tab:red")
ax[0].plot(new_x, Gaussian(new_x, params[0].get("amplitude")[2,0], params[0].get("mean")[2,0], params[0].get("sigma")[2,0]), color="tab:red")
ax[0].text(5200, 21000, str(round(params[0].get("R[%]")[0,0],2)) + "(" + str(round(params[0].get("R[%]")[0,1],2)) + ")" + "\%" )
ax[0].text(5530, 19000, str(round(params[0].get("R[%]")[1,0],2)) + "(" + str(round(params[0].get("R[%]")[1,1],2)) + ")" + "\%" )
ax[0].text(5700, 12000, str(round(params[0].get("R[%]")[2,0],2)) + "(" + str(round(params[0].get("R[%]")[2,1],2)) + ")" + "\%" )
ax[1].plot(new_x, Gaussian(new_x, params[1].get("amplitude")[0,0], params[1].get("mean")[0,0], params[1].get("sigma")[0,0]), color="tab:red")
ax[1].plot(new_x, Gaussian(new_x, params[1].get("amplitude")[1,0], params[1].get("mean")[1,0], params[1].get("sigma")[1,0]), color="tab:red")
ax[1].plot(new_x, Gaussian(new_x, params[1].get("amplitude")[2,0], params[1].get("mean")[2,0], params[1].get("sigma")[2,0]), color="tab:red")
ax[1].text(5200, 11500, str(round(params[1].get("R[%]")[0,0],2)) + "(" + str(round(params[1].get("R[%]")[0,1],2)) + ")" + "\%" )
ax[1].text(5530, 11000, str(round(params[1].get("R[%]")[1,0],2)) + "(" + str(round(params[1].get("R[%]")[1,1],2)) + ")" + "\%" )
ax[1].text(5700, 6500, str(round(params[1].get("R[%]")[2,0],2)) + "(" + str(round(params[1].get("R[%]")[2,1],2)) + ")" + "\%" )
ax[2].plot(new_x, Gaussian(new_x, params[2].get("amplitude")[0,0], params[2].get("mean")[0,0], params[2].get("sigma")[0,0]), color="tab:red")
ax[2].plot(new_x, Gaussian(new_x, params[2].get("amplitude")[1,0], params[2].get("mean")[1,0], params[2].get("sigma")[1,0]), color="tab:red")
ax[2].plot(new_x, Gaussian(new_x, params[2].get("amplitude")[2,0], params[2].get("mean")[2,0], params[2].get("sigma")[2,0]), color="tab:red")
ax[2].text(5200, 6000, str(round(params[2].get("R[%]")[0,0],2)) + "(" + str(round(params[2].get("R[%]")[0,1],2)) + ")" + "\%" )
ax[2].text(5530, 5500, str(round(params[2].get("R[%]")[1,0],2)) + "(" + str(round(params[2].get("R[%]")[1,1],2)) + ")" + "\%" )
ax[2].text(5700, 3000, str(round(params[2].get("R[%]")[2,0],2)) + "(" + str(round(params[2].get("R[%]")[2,1],2)) + ")" + "\%" )
ax[0].set_xlim(5000,6000)
ax[1].set_xlim(5000,6000)
ax[2].set_xlim(5000,6000)
ax[0].set_ylim(0)
ax[1].set_ylim(0)
ax[2].set_ylim(0)
ax[0].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[2].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0].set_ylabel("Counts")
ax[0].set_xlabel("Energy (keV)")
ax[1].set_xlabel("Energy (keV)")
ax[2].set_xlabel("Energy (keV)")
ax[0].set_title("Energy gain = 1")
ax[1].set_title("Energy gain = 2")
ax[2].set_title("Energy gain = 4")
plt.suptitle("Gain test")
plt.show()