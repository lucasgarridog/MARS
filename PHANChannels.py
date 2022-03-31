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

# Code used to study the resolution dependence on the number of channels

### CODE ###
# Data loading
folder = r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA_test\NChannels"
run_1 = CompassLoader(folder + "\HCompassF_run_1_20220328.root")
run_2 = CompassLoader(folder + "\HCompassF_run_2_20220328.root")
run_3 = CompassLoader(folder + "\HCompassF_run_3_20220328.root")
run_4 = CompassLoader(folder + "\HCompassF_run_4_20220328.root")
# Data calibration
energies = [5156.59, 5485.56, 5804.82]
cal_fit, calibrated_x = SpectraCalibrator(run_1[0,:], run_1[1,:], energies)
run_1[0,:] = calibrated_x
cal_fit, calibrated_x = SpectraCalibrator(run_2[0,:], run_2[1,:], energies)
run_2[0,:] = calibrated_x
cal_fit, calibrated_x = SpectraCalibrator(run_3[0,:], run_3[1,:], energies)
run_3[0,:] = calibrated_x
cal_fit, calibrated_x = SpectraCalibrator(run_4[0,:], run_4[1,:], energies)
run_4[0,:] = calibrated_x
# Data analysis
fit_1 = Gaussian_fit_spectra(run_1[0,:], run_1[1,:], plot=False)
fit_2 = Gaussian_fit_spectra(run_2[0,:], run_2[1,:], plot=False)
fit_3 = Gaussian_fit_spectra(run_3[0,:], run_3[1,:], plot=False)
fit_4 = Gaussian_fit_spectra(run_4[0,:], run_4[1,:], plot=False)

# Plot
new_x = np.linspace(5000,6000,1000)
f, ax = plt.subplots(1, 4, figsize=(17,9))
ax[0].step(run_1[0,:], run_1[1,:], color="tab:blue")
ax[0].fill_between(run_1[0,:], run_1[1,:], color="tab:blue", step="pre")
ax[1].step(run_2[0,:], run_2[1,:], color="tab:blue")
ax[1].fill_between(run_2[0,:], run_2[1,:], color="tab:blue", step="pre")
ax[2].step(run_3[0,:], run_3[1,:], color="tab:blue")
ax[2].fill_between(run_3[0,:], run_3[1,:], color="tab:blue", step="pre")
ax[3].step(run_4[0,:], run_4[1,:], color="tab:blue")
ax[3].fill_between(run_4[0,:], run_4[1,:], color="tab:blue", step="pre")
ax[0].plot(new_x, Gaussian(new_x, fit_1.get("amplitude")[0,0], fit_1.get("mean")[0,0], fit_1.get("sigma")[0,0]), color="tab:red")
ax[0].plot(new_x, Gaussian(new_x, fit_1.get("amplitude")[1,0], fit_1.get("mean")[1,0], fit_1.get("sigma")[1,0]), color="tab:red")
ax[0].plot(new_x, Gaussian(new_x, fit_1.get("amplitude")[2,0], fit_1.get("mean")[2,0], fit_1.get("sigma")[2,0]), color="tab:red")
ax[0].text(5200, 13800, str(round(fit_1.get("R[%]")[0,0],2)) + "(" + str(round(fit_1.get("R[%]")[0,1],2)) + ")" + "\%" )
ax[0].text(5530, 11000, str(round(fit_1.get("R[%]")[1,0],2)) + "(" + str(round(fit_1.get("R[%]")[1,1],2)) + ")" + "\%" )
ax[0].text(5600, 7000, str(round(fit_1.get("R[%]")[2,0],2)) + "(" + str(round(fit_1.get("R[%]")[2,1],2)) + ")" + "\%" )
ax[1].plot(new_x, Gaussian(new_x, fit_2.get("amplitude")[0,0], fit_2.get("mean")[0,0], fit_2.get("sigma")[0,0]), color="tab:red")
ax[1].plot(new_x, Gaussian(new_x, fit_2.get("amplitude")[1,0], fit_2.get("mean")[1,0], fit_2.get("sigma")[1,0]), color="tab:red")
ax[1].plot(new_x, Gaussian(new_x, fit_2.get("amplitude")[2,0], fit_2.get("mean")[2,0], fit_2.get("sigma")[2,0]), color="tab:red")
ax[1].text(5200, 6000, str(round(fit_2.get("R[%]")[0,0],2)) + "(" + str(round(fit_2.get("R[%]")[0,1],2)) + ")" + "\%" )
ax[1].text(5530, 5800, str(round(fit_2.get("R[%]")[1,0],2)) + "(" + str(round(fit_2.get("R[%]")[1,1],2)) + ")" + "\%" )
ax[1].text(5600, 3000, str(round(fit_2.get("R[%]")[2,0],2)) + "(" + str(round(fit_2.get("R[%]")[2,1],2)) + ")" + "\%" )
ax[2].plot(new_x, Gaussian(new_x, fit_3.get("amplitude")[0,0], fit_3.get("mean")[0,0], fit_3.get("sigma")[0,0]), color="tab:red")
ax[2].plot(new_x, Gaussian(new_x, fit_3.get("amplitude")[1,0], fit_3.get("mean")[1,0], fit_3.get("sigma")[1,0]), color="tab:red")
ax[2].plot(new_x, Gaussian(new_x, fit_3.get("amplitude")[2,0], fit_3.get("mean")[2,0], fit_3.get("sigma")[2,0]), color="tab:red")
ax[2].text(5200, 3000, str(round(fit_3.get("R[%]")[0,0],2)) + "(" + str(round(fit_3.get("R[%]")[0,1],2)) + ")" + "\%" )
ax[2].text(5530, 2800, str(round(fit_3.get("R[%]")[1,0],2)) + "(" + str(round(fit_3.get("R[%]")[1,1],2)) + ")" + "\%" )
ax[2].text(5600, 1600, str(round(fit_3.get("R[%]")[2,0],2)) + "(" + str(round(fit_3.get("R[%]")[2,1],2)) + ")" + "\%" )
ax[3].plot(new_x, Gaussian(new_x, fit_4.get("amplitude")[0,0], fit_4.get("mean")[0,0], fit_4.get("sigma")[0,0]), color="tab:red")
ax[3].plot(new_x, Gaussian(new_x, fit_4.get("amplitude")[1,0], fit_4.get("mean")[1,0], fit_4.get("sigma")[1,0]), color="tab:red")
ax[3].plot(new_x, Gaussian(new_x, fit_4.get("amplitude")[2,0], fit_4.get("mean")[2,0], fit_4.get("sigma")[2,0]), color="tab:red")
ax[3].text(5200, 1500, str(round(fit_4.get("R[%]")[0,0],2)) + "(" + str(round(fit_4.get("R[%]")[0,1],2)) + ")" + "\%" )
ax[3].text(5530, 1400, str(round(fit_4.get("R[%]")[1,0],2)) + "(" + str(round(fit_4.get("R[%]")[1,1],2)) + ")" + "\%" )
ax[3].text(5600, 800, str(round(fit_4.get("R[%]")[2,0],2)) + "(" + str(round(fit_4.get("R[%]")[2,1],2)) + ")" + "\%" )
ax[0].set_xlim(5000,6000)
ax[1].set_xlim(5000,6000)
ax[2].set_xlim(5000,6000)
ax[3].set_xlim(5000,6000)
ax[0].set_ylim(0)
ax[1].set_ylim(0)
ax[2].set_ylim(0)
ax[3].set_ylim(0)
ax[0].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[2].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[3].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0].set_ylabel("Counts")
ax[0].set_xlabel("Energy (keV)")
ax[1].set_xlabel("Energy (keV)")
ax[2].set_xlabel("Energy (keV)")
ax[3].set_xlabel("Energy (keV)")
ax[0].set_title("Channels = 2048")
ax[1].set_title("Channels = 4096")
ax[2].set_title("Channels = 8192")
ax[3].set_title("Channels = 16384")
plt.suptitle("N Channels test")
plt.show()