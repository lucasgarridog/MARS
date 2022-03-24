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

# Code used to analyze the first measurements with PHA firmware

### CODE ###
# Data loading
folder = r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA_test"
data = CompassLoader(folder + "\HcompassF_run_1_20220323.root")

# Data calibration
energies = [5156.59, 5485.56, 5804.82]
cal_fit, calibrated_x = SpectraCalibrator(data[0,:], data[1,:], energies)

# Data analysis
fit = Gaussian_fit_spectra(calibrated_x, data[1,:], plot=False)

# Plot
plt.step(calibrated_x, data[1,:], color="tab:blue")
plt.plot(calibrated_x, Gaussian(calibrated_x, fit.get("amplitude")[0,0], fit.get("mean")[0,0], fit.get("sigma")[0,0]), color="tab:red")
plt.plot(calibrated_x, Gaussian(calibrated_x, fit.get("amplitude")[1,0], fit.get("mean")[1,0], fit.get("sigma")[1,0]), color="tab:red")
plt.plot(calibrated_x, Gaussian(calibrated_x, fit.get("amplitude")[2,0], fit.get("mean")[2,0], fit.get("sigma")[2,0]), color="tab:red")
plt.fill_between(calibrated_x, data[1,:], color="tab:blue", step="pre")
plt.text(5200, 8000, str(round(fit.get("R[%]")[0,0],2)) + "\%")
plt.text(5520, 8000, str(round(fit.get("R[%]")[1,0],2)) + "\%")
plt.text(5840, 4000, str(round(fit.get("R[%]")[2,0],2)) + "\%")
plt.xlim(5000,6000)
plt.ylim(0)
plt.ticklabel_format(axis="y", style="sci", scilimits=(3,3))
plt.ylabel("Counts")
plt.xlabel("Energy (keV)")
plt.title("PHA firmware test")
plt.show()