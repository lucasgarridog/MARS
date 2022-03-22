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

# Code used to analyze the effect of changing some parameters
# of the trapezoid filter in COMPASS (calibrated version)

### CODE ###
# Data loading
folder = r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\Trapezoid_tests"
runs = range(1,15)                                          # there are 14 runs
data = np.zeros((2,4095,14))                                # 2 lines (x,y) and 4095 channels
for run in runs:
    data[:,:,run-1] = CompassLoader(folder + "\HcompassF_run_" + str(run) + "_20220316.root")

ref = np.loadtxt(folder + "/triple_alpha.txt")              # this is the spectrum i emulated
x_ref = range(len(ref))

# Calibration of each run (except 10, which is a mess)
energies = [5156.59, 5485.56, 5804.82]
data_calibrated = data
for run in runs:
    if run == 10:
        continue
    fit, calibrated_x = SpectraCalibrator(data[0,:,run-1], data[1,:,run-1], energies)
    data_calibrated[0,:,run - 1] = calibrated_x

_, calibrated_ref = SpectraCalibrator(x_ref, ref, energies, plot=False)

# Data analysis (except 10, which is a mess)
params = []
R = []
for run in runs:
    fit = Gaussian_fit_spectra(data_calibrated[0,:,run-1], data_calibrated[1,:,run-1], plot=False)
    params.append(fit)
    R.append(fit.get("R[%]"))

# ref_fit = Gaussian_fit_spectra(calibrated_ref, ref, plot=False)    # solo funciona cambiando en Fits.py el y/2
# print(ref_fit)
# plt.step(calibrated_ref, ref, color="tab:blue")
# plt.fill_between(calibrated_ref, ref, color="tab:blue", step="pre")
# plt.plot(calibrated_ref, Gaussian(calibrated_ref, ref_fit.get("amplitude")[0,0], ref_fit.get("mean")[0,0], ref_fit.get("sigma")[0,0]), color="tab:red")
# plt.plot(calibrated_ref, Gaussian(calibrated_ref, ref_fit.get("amplitude")[1,0], ref_fit.get("mean")[1,0], ref_fit.get("sigma")[1,0]), color="tab:red")
# plt.plot(calibrated_ref, Gaussian(calibrated_ref, ref_fit.get("amplitude")[2,0], ref_fit.get("mean")[2,0], ref_fit.get("sigma")[2,0]), color="tab:red")
# plt.text(5200, 1500, str(round(ref_fit.get("R[%]")[0,0],2)) + "\%")
# plt.text(5500, 1600, str(round(ref_fit.get("R[%]")[1,0],2)) + "\%")
# plt.text(5820, 650, str(round(ref_fit.get("R[%]")[2,0],2)) + "\%")
# plt.xlabel("Energy (keV)")
# plt.ylabel("Counts")
# plt.title("Simulated spectrum")
# plt.xlim(5000,6000)
# plt.ylim(0)
# plt.show()


# Changing rise time (runs 1 - 3)
f, ax = plt.subplots(1, 3, figsize=(16,8))
ax[0].step(data_calibrated[0,:,0], data_calibrated[1,:,0], color="tab:blue")
ax[0].plot(data_calibrated[0,:,0], Gaussian(data_calibrated[0,:,0], params[0].get("amplitude")[0,0], params[0].get("mean")[0,0], params[0].get("sigma")[0,0]), color="tab:red")
ax[0].plot(data_calibrated[0,:,0], Gaussian(data_calibrated[0,:,0], params[0].get("amplitude")[1,0], params[0].get("mean")[1,0], params[0].get("sigma")[1,0]), color="tab:red")
ax[0].plot(data_calibrated[0,:,0], Gaussian(data_calibrated[0,:,0], params[0].get("amplitude")[2,0], params[0].get("mean")[2,0], params[0].get("sigma")[2,0]), color="tab:red")
ax[0].fill_between(data_calibrated[0,:,0], data_calibrated[1,:,0], color="tab:blue", step="pre")
ax[0].text(5200, 35000, str(round(R[0][0][0],2)) + "\%")
ax[0].text(5500, 30000, str(round(R[0][1][0],2)) + "\%")
ax[0].text(5820, 12000, str(round(R[0][2][0],2)) + "\%")
ax[1].step(data_calibrated[0,:,1], data_calibrated[1,:,1], color="tab:blue")
ax[1].plot(data_calibrated[0,:,1], Gaussian(data_calibrated[0,:,1], params[1].get("amplitude")[0,0], params[1].get("mean")[0,0], params[1].get("sigma")[0,0]), color="tab:red")
ax[1].plot(data_calibrated[0,:,1], Gaussian(data_calibrated[0,:,1], params[1].get("amplitude")[1,0], params[1].get("mean")[1,0], params[1].get("sigma")[1,0]), color="tab:red")
ax[1].plot(data_calibrated[0,:,1], Gaussian(data_calibrated[0,:,1], params[1].get("amplitude")[2,0], params[1].get("mean")[2,0], params[1].get("sigma")[2,0]), color="tab:red")
ax[1].fill_between(data_calibrated[0,:,1], data_calibrated[1,:,1], color="tab:blue", step="pre")
ax[1].text(5200, 4100, str(round(R[1][0][0],2)) + "\%")
ax[1].text(5500, 3000, str(round(R[1][1][0],2)) + "\%")
ax[1].text(5820, 1200, str(round(R[1][2][0],2)) + "\%")
ax[2].step(data_calibrated[0,:,2], data_calibrated[1,:,2], color="tab:blue")
ax[2].fill_between(data_calibrated[0,:,2], data_calibrated[1,:,2], color="tab:blue", step="pre")
ax[2].plot(data_calibrated[0,:,2], Gaussian(data_calibrated[0,:,2], params[2].get("amplitude")[0,0], params[2].get("mean")[0,0], params[2].get("sigma")[0,0]), color="tab:red")
ax[2].plot(data_calibrated[0,:,2], Gaussian(data_calibrated[0,:,2], params[2].get("amplitude")[1,0], params[2].get("mean")[1,0], params[2].get("sigma")[1,0]), color="tab:red")
ax[2].plot(data_calibrated[0,:,2], Gaussian(data_calibrated[0,:,2], params[2].get("amplitude")[2,0], params[2].get("mean")[2,0], params[2].get("sigma")[2,0]), color="tab:red")
ax[2].text(5200, 2900, str(round(R[2][0][0],2)) + "\%")
ax[2].text(5500, 1800, str(round(R[2][1][0],2)) + "\%")
ax[2].text(5820, 650, str(round(R[2][2][0],2)) + "\%")
ax[0].set_xlim(4200,6200)
ax[1].set_xlim(4200,6200)
ax[2].set_xlim(4200,6200)
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
ax[0].set_title("Rise time = 0.016 $\mu$s")
ax[1].set_title("Rise time = 0.032 $\mu$s")
ax[2].set_title("Rise time = 0.064 $\mu$s")
plt.suptitle("Runs 1-3")

# Changing flat top (runs 4 - 9)
f, ax = plt.subplots(2, 3, figsize=(16,8))
ax[0,0].step(data_calibrated[0,:,3], data_calibrated[1,:,3], color="tab:blue")
ax[0,0].plot(data_calibrated[0,:,3], Gaussian(data_calibrated[0,:,3], params[3].get("amplitude")[0,0], params[3].get("mean")[0,0], params[3].get("sigma")[0,0]), color="tab:red")
ax[0,0].plot(data_calibrated[0,:,3], Gaussian(data_calibrated[0,:,3], params[3].get("amplitude")[1,0], params[3].get("mean")[1,0], params[3].get("sigma")[1,0]), color="tab:red")
ax[0,0].plot(data_calibrated[0,:,3], Gaussian(data_calibrated[0,:,3], params[3].get("amplitude")[2,0], params[3].get("mean")[2,0], params[3].get("sigma")[2,0]), color="tab:red")
ax[0,0].fill_between(data_calibrated[0,:,3], data_calibrated[1,:,3], color="tab:blue", step="pre")
ax[0,0].set_ylim(0)
ax[0,0].set_xlim(4200,6200)
ax[0,0].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0,0].set_ylabel("Counts")
ax[0,0].set_title("Flat top = 0.496 $\mu$s")
ax[0,1].step(data_calibrated[0,:,4], data_calibrated[1,:,4], color="tab:blue")
ax[0,1].plot(data_calibrated[0,:,4], Gaussian(data_calibrated[0,:,4], params[4].get("amplitude")[0,0], params[4].get("mean")[0,0], params[4].get("sigma")[0,0]), color="tab:red")
ax[0,1].plot(data_calibrated[0,:,4], Gaussian(data_calibrated[0,:,4], params[4].get("amplitude")[1,0], params[4].get("mean")[1,0], params[4].get("sigma")[1,0]), color="tab:red")
ax[0,1].plot(data_calibrated[0,:,4], Gaussian(data_calibrated[0,:,4], params[4].get("amplitude")[2,0], params[4].get("mean")[2,0], params[4].get("sigma")[2,0]), color="tab:red")
ax[0,1].fill_between(data_calibrated[0,:,4], data_calibrated[1,:,4], color="tab:blue", step="pre")
ax[0,1].set_ylim(0)
ax[0,1].set_xlim(4200,6200)
ax[0,1].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0,1].set_ylabel("Counts")
ax[0,1].set_title("Flat top = 0.192 $\mu$s")
ax[0,2].step(data_calibrated[0,:,5], data_calibrated[1,:,5], color="tab:blue")
ax[0,2].plot(data_calibrated[0,:,5], Gaussian(data_calibrated[0,:,5], params[5].get("amplitude")[0,0], params[5].get("mean")[0,0], params[5].get("sigma")[0,0]), color="tab:red")
ax[0,2].plot(data_calibrated[0,:,5], Gaussian(data_calibrated[0,:,5], params[5].get("amplitude")[1,0], params[5].get("mean")[1,0], params[5].get("sigma")[1,0]), color="tab:red")
ax[0,2].plot(data_calibrated[0,:,5], Gaussian(data_calibrated[0,:,5], params[5].get("amplitude")[2,0], params[5].get("mean")[2,0], params[5].get("sigma")[2,0]), color="tab:red")
ax[0,2].fill_between(data_calibrated[0,:,5], data_calibrated[1,:,5], color="tab:blue", step="pre")
ax[0,2].set_ylim(0)
ax[0,2].set_xlim(4200,6200)
ax[0,2].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0,2].set_ylabel("Counts")
ax[0,2].set_title("Flat top = 0.064 $\mu$s")
ax[1,0].step(data_calibrated[0,:,6], data_calibrated[1,:,6], color="tab:blue")
ax[1,0].plot(data_calibrated[0,:,6], Gaussian(data_calibrated[0,:,6], params[6].get("amplitude")[0,0], params[6].get("mean")[0,0], params[6].get("sigma")[0,0]), color="tab:red")
ax[1,0].plot(data_calibrated[0,:,6], Gaussian(data_calibrated[0,:,6], params[6].get("amplitude")[1,0], params[6].get("mean")[1,0], params[6].get("sigma")[1,0]), color="tab:red")
ax[1,0].plot(data_calibrated[0,:,6], Gaussian(data_calibrated[0,:,6], params[6].get("amplitude")[2,0], params[6].get("mean")[2,0], params[6].get("sigma")[2,0]), color="tab:red")
ax[1,0].fill_between(data_calibrated[0,:,6], data_calibrated[1,:,6], color="tab:blue", step="pre")
ax[1,0].set_ylim(0)
ax[1,0].set_xlim(4200,6200)
ax[1,0].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1,0].set_ylabel("Counts")
ax[1,0].set_xlabel("Energy (keV)")
ax[1,0].set_title("Flat top = 0.016 $\mu$s")
ax[1,1].step(data_calibrated[0,:,7], data_calibrated[1,:,7], color="tab:blue")
ax[1,1].plot(data_calibrated[0,:,7], Gaussian(data_calibrated[0,:,7], params[7].get("amplitude")[0,0], params[7].get("mean")[0,0], params[7].get("sigma")[0,0]), color="tab:red")
ax[1,1].plot(data_calibrated[0,:,7], Gaussian(data_calibrated[0,:,7], params[7].get("amplitude")[1,0], params[7].get("mean")[1,0], params[7].get("sigma")[1,0]), color="tab:red")
ax[1,1].plot(data_calibrated[0,:,7], Gaussian(data_calibrated[0,:,7], params[7].get("amplitude")[2,0], params[7].get("mean")[2,0], params[7].get("sigma")[2,0]), color="tab:red")
ax[1,1].fill_between(data_calibrated[0,:,7], data_calibrated[1,:,7], color="tab:blue", step="pre")
ax[1,1].set_ylim(0)
ax[1,1].set_xlim(4200,6200)
ax[1,1].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1,1].set_ylabel("Counts")
ax[1,1].set_xlabel("Energy (keV)")
ax[1,1].set_title("Flat top = 0.016 $\mu$s")
ax[1,2].step(data_calibrated[0,:,8], data_calibrated[1,:,8], color="tab:blue")
ax[1,2].plot(data_calibrated[0,:,8], Gaussian(data_calibrated[0,:,8], params[8].get("amplitude")[0,0], params[8].get("mean")[0,0], params[8].get("sigma")[0,0]), color="tab:red")
ax[1,2].plot(data_calibrated[0,:,8], Gaussian(data_calibrated[0,:,8], params[8].get("amplitude")[1,0], params[8].get("mean")[1,0], params[8].get("sigma")[1,0]), color="tab:red")
ax[1,2].plot(data_calibrated[0,:,8], Gaussian(data_calibrated[0,:,8], params[8].get("amplitude")[2,0], params[8].get("mean")[2,0], params[8].get("sigma")[2,0]), color="tab:red")
ax[1,2].fill_between(data_calibrated[0,:,8], data_calibrated[1,:,8], color="tab:blue", step="pre")
ax[1,2].set_ylim(0)
ax[1,2].set_xlim(4200,6200)
ax[1,2].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1,2].set_ylabel("Counts")
ax[1,2].set_xlabel("Energy (keV)")
ax[1,2].set_title("Flat top = 2 $\mu$s")
ax[0,0].text(5200, 3200, str(round(R[3][0][0],2)) + "\%")
ax[0,0].text(5500, 2200, str(round(R[3][1][0],2)) + "\%")
ax[0,0].text(5820, 1000, str(round(R[3][2][0],2)) + "\%")
ax[0,1].text(5200, 3400, str(round(R[4][0][0],2)) + "\%")
ax[0,1].text(5500, 2200, str(round(R[4][1][0],2)) + "\%")
ax[0,1].text(5820, 1000, str(round(R[4][2][0],2)) + "\%")
ax[0,2].text(5200, 3400, str(round(R[5][0][0],2)) + "\%")
ax[0,2].text(5500, 2200, str(round(R[5][1][0],2)) + "\%")
ax[0,2].text(5820, 1000, str(round(R[5][2][0],2)) + "\%")
ax[1,0].text(5200, 4000, str(round(R[6][0][0],2)) + "\%")
ax[1,0].text(5500, 2500, str(round(R[6][1][0],2)) + "\%")
ax[1,0].text(5820, 1000, str(round(R[6][2][0],2)) + "\%")
ax[1,1].text(5200, 4000, str(round(R[7][0][0],2)) + "\%")
ax[1,1].text(5500, 2500, str(round(R[7][1][0],2)) + "\%")
ax[1,1].text(5820, 1000, str(round(R[7][2][0],2)) + "\%")
ax[1,2].text(5200, 4000, str(round(R[8][0][0],2)) + "\%")
ax[1,2].text(5500, 2500, str(round(R[8][1][0],2)) + "\%")
ax[1,2].text(5820, 1000, str(round(R[8][2][0],2)) + "\%")
plt.suptitle("Runs 4-9")

# Changing energy fine gain (runs 11 - 14)
f, ax = plt.subplots(2, 2, figsize=(16,8))
ax[0,0].step(data_calibrated[0,:,10], data_calibrated[1,:,10], color="tab:blue")
ax[0,0].plot(data_calibrated[0,:,10], Gaussian(data_calibrated[0,:,10], params[10].get("amplitude")[0,0], params[10].get("mean")[0,0], params[10].get("sigma")[0,0]), color="tab:red")
ax[0,0].plot(data_calibrated[0,:,10], Gaussian(data_calibrated[0,:,10], params[10].get("amplitude")[1,0], params[10].get("mean")[1,0], params[10].get("sigma")[1,0]), color="tab:red")
ax[0,0].plot(data_calibrated[0,:,10], Gaussian(data_calibrated[0,:,10], params[10].get("amplitude")[2,0], params[10].get("mean")[2,0], params[10].get("sigma")[2,0]), color="tab:red")
ax[0,0].fill_between(data_calibrated[0,:,10], data_calibrated[1,:,10], color="tab:blue", step="pre")
ax[0,0].set_ylim(0)
ax[0,0].set_xlim(4200,6200)
ax[0,0].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0,0].set_ylabel("Counts")
ax[0,0].set_title("Energy fine gain = 1")
ax[0,1].step(data_calibrated[0,:,11], data_calibrated[1,:,11], color="tab:blue")
ax[0,1].plot(data_calibrated[0,:,11], Gaussian(data_calibrated[0,:,11], params[11].get("amplitude")[0,0], params[11].get("mean")[0,0], params[11].get("sigma")[0,0]), color="tab:red")
ax[0,1].plot(data_calibrated[0,:,11], Gaussian(data_calibrated[0,:,11], params[11].get("amplitude")[1,0], params[11].get("mean")[1,0], params[11].get("sigma")[1,0]), color="tab:red")
ax[0,1].plot(data_calibrated[0,:,11], Gaussian(data_calibrated[0,:,11], params[11].get("amplitude")[2,0], params[11].get("mean")[2,0], params[11].get("sigma")[2,0]), color="tab:red")
ax[0,1].fill_between(data_calibrated[0,:,11], data_calibrated[1,:,11], color="tab:blue", step="pre")
ax[0,1].set_ylim(0)
ax[0,1].set_xlim(4200,6200)
ax[0,1].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[0,1].set_ylabel("Counts")
ax[0,1].set_title("Energy fine gain = 4")
ax[1,0].step(data_calibrated[0,:,12], data_calibrated[1,:,12], color="tab:blue")
ax[1,0].plot(data_calibrated[0,:,12], Gaussian(data_calibrated[0,:,12], params[12].get("amplitude")[0,0], params[12].get("mean")[0,0], params[12].get("sigma")[0,0]), color="tab:red")
ax[1,0].plot(data_calibrated[0,:,12], Gaussian(data_calibrated[0,:,12], params[12].get("amplitude")[1,0], params[12].get("mean")[1,0], params[12].get("sigma")[1,0]), color="tab:red")
ax[1,0].plot(data_calibrated[0,:,12], Gaussian(data_calibrated[0,:,12], params[12].get("amplitude")[2,0], params[12].get("mean")[2,0], params[12].get("sigma")[2,0]), color="tab:red")
ax[1,0].fill_between(data_calibrated[0,:,12], data_calibrated[1,:,12], color="tab:blue", step="pre")
ax[1,0].set_ylim(0)
ax[1,0].set_xlim(4200,6200)
ax[1,0].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1,0].set_ylabel("Counts")
ax[1,0].set_title("Energy fine gain = 6")
ax[1,1].step(data_calibrated[0,:,13], data_calibrated[1,:,13], color="tab:blue")
ax[1,1].plot(data_calibrated[0,:,13], Gaussian(data_calibrated[0,:,13], params[13].get("amplitude")[0,0], params[13].get("mean")[0,0], params[13].get("sigma")[0,0]), color="tab:red")
ax[1,1].plot(data_calibrated[0,:,13], Gaussian(data_calibrated[0,:,13], params[13].get("amplitude")[1,0], params[13].get("mean")[1,0], params[13].get("sigma")[1,0]), color="tab:red")
ax[1,1].plot(data_calibrated[0,:,13], Gaussian(data_calibrated[0,:,13], params[13].get("amplitude")[2,0], params[13].get("mean")[2,0], params[13].get("sigma")[2,0]), color="tab:red")
ax[1,1].fill_between(data_calibrated[0,:,13], data_calibrated[1,:,13], color="tab:blue", step="pre")
ax[1,1].set_ylim(0)
ax[1,1].set_xlim(4200,6200)
ax[1,1].ticklabel_format(axis="y", style="sci", scilimits=(3,3))
ax[1,1].set_ylabel("Counts")
ax[1,1].set_title("Energy fine gain = 9")
ax[0,0].text(5200, 6300, str(round(R[10][0][0],2)) + "\%")
ax[0,0].text(5500, 5000, str(round(R[10][1][0],2)) + "\%")
ax[0,0].text(5820, 2000, str(round(R[10][2][0],2)) + "\%")
ax[0,1].text(5200, 2000, str(round(R[11][0][0],2)) + "\%")
ax[0,1].text(5500, 1500, str(round(R[11][1][0],2)) + "\%")
ax[0,1].text(5820, 800, str(round(R[11][2][0],2)) + "\%")
ax[1,0].text(5200, 2200, str(round(R[12][0][0],2)) + "\%")
ax[1,0].text(5500, 1900, str(round(R[12][1][0],2)) + "\%")
ax[1,0].text(5820, 900, str(round(R[12][2][0],2)) + "\%")
ax[1,1].text(5200, 1500, str(round(R[13][0][0],2)) + "\%")
ax[1,1].text(5500, 1300, str(round(R[13][1][0],2)) + "\%")
ax[1,1].text(5820, 600, str(round(R[13][2][0],2)) + "\%")
ax[1,0].set_xlabel("Energy (keV)")
ax[1,1].set_xlabel("Energy (keV)")
plt.suptitle("Runs 11-14")

# Bar plot
resolutions = []
i = 0
while i < 3:
    resolutions.append([R[0][i][0], R[1][i][0], R[2][i][0], R[3][i][0], R[4][i][0], R[5][i][0], R[6][i][0], R[7][i][0], R[8][i][0], R[10][i][0], R[11][i][0], R[12][i][0], R[13][i][0]])
    i = i + 1

x = [str(1),str(2),str(3),str(4),str(5),str(6),str(7),str(8),str(9),str(11),str(12),str(13),str(14)]
aux = np.arange(13)

f = plt.figure(figsize=(16,8))
plt.bar(aux, resolutions[0], color="tab:blue", width=0.2, label="Peak 1")
plt.bar(aux + 0.25, resolutions[1], color="tab:red", width=0.2, label="Peak 2")
plt.bar(aux + 0.5, resolutions[2], color="tab:green", width=0.2, label="Peak 3")
plt.xlabel("\# run")
plt.ylabel("Resolution (\%)")
plt.ylim(1,5)
plt.xticks( aux + 0.25 , x)
plt.legend()
plt.title("Peak resolution for each run")
plt.show()