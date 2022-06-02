# INITIALIZATION
import sys
import matplotlib.pyplot as plt
sys.path.append(r"C:\Users\Lucas Garrido\Documents\PhD\Codigo\Functions")
from CompassLoader import *
from Spectrum import *

# DATA LOADING, CALIBRATION AND FITTING
channels = np.arange(16)
data = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_PHA_MaxV.root")
data2 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_PHA_MaxV_run2.root")
data5 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_PHA_MaxV_run3.root")
data10 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_PHA_MaxV_run4.root")
data12 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_PHA_MaxV_run5.root")
data15 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_PHA_MaxV_run6.root")
data20 = CompassLoader(r"C:\Users\Lucas Garrido\Documents\PhD\Measurements\PHA\HcompassF_PHA_MaxV_run7.root")
spectra = []
spectra2 = []
spectra5 = []
spectra10 = []
spectra12 = []
spectra15 = []
spectra20 = []
energies = [5.156, 5.485, 5.804]                                         # Pu-239, Am-241 and Cm-244 in keV
for channel in channels:
    spectra.append(Spectrum(data[0,:,channel], data[1,:,channel]))    # the 16 spectra of the 16 channels
    spectra2.append(Spectrum(data2[0,:,channel], data2[1,:,channel]))    # the 16 spectra of the 16 channels
    spectra5.append(Spectrum(data5[0,:,channel], data5[1,:,channel]))    # the 16 spectra of the 16 channels
    spectra10.append(Spectrum(data10[0,:,channel], data10[1,:,channel]))    # the 16 spectra of the 16 channels
    spectra12.append(Spectrum(data12[0,:,channel], data12[1,:,channel]))    # the 16 spectra of the 16 channels
    spectra15.append(Spectrum(data15[0,:,channel], data15[1,:,channel]))    # the 16 spectra of the 16 channels
    spectra20.append(Spectrum(data20[0,:,channel], data20[1,:,channel]))    # the 16 spectra of the 16 channels

calibrated_x, fit = spectra[0].calibrate(energies, unit=1)

spectra2[0].Evals = calibrated_x
spectra2[0].is_calibrated = True
spectra5[0].Evals = calibrated_x
spectra5[0].is_calibrated = True
spectra10[0].Evals = calibrated_x
spectra10[0].is_calibrated = True
spectra12[0].Evals = calibrated_x
spectra12[0].is_calibrated = True
spectra15[0].Evals = calibrated_x
spectra15[0].is_calibrated = True
spectra20[0].Evals = calibrated_x
spectra20[0].is_calibrated = True

spectra[0].plot(unit=1)
spectra2[0].plot(unit=1)
spectra5[0].plot(unit=1)
spectra10[0].plot(unit=1)
spectra12[0].plot(unit=1)
spectra15[0].plot(unit=1)
spectra20[0].plot(unit=1)
