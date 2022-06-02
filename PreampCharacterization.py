# INITIALIZATION
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(r"C:\Users\Lucas Garrido\Documents\PhD\Codigo\Functions")
from CompassLoader import *
from Spectrum import *
plt.rcParams['font.size'] = 22
plt.rcParams['figure.figsize'] = (9, 7)

##### VOLTAJES, TODAS LAS MAGNITUDES EN VOLTIOS ####
vout_pulser = [-0.26, -0.33, -0.39, -0.46, -0.53, -0.59, -0.66]
vout_12324_ch1 = [0.30, 0.38, 0.45, 0.53, 0.61, 0.68, 0.75]
vout_12324_ch2 = [0.29, 0.37, 0.44, 0.51, 0.59, 0.66, 0.73]
vout_12324_ch3 = [0.30, 0.38, 0.46, 0.53, 0.61, 0.68, 0.75]
vout_12324_ch4 = [0.31, 0.36, 0.43, 0.50, 0.57, 0.64, 0.72]
vout_12324_ch5 = [0.28, 0.35, 0.42, 0.49, 0.56, 0.63, 0.70]
vout_12324_ch6 = [0.30, 0.38, 0.45, 0.52, 0.60, 0.67, 0.74]
vout_12324_ch7 = [0.29, 0.36, 0.43, 0.50, 0.58, 0.65, 0.72]
vout_12324_ch8 = [0.27, 0.35, 0.42, 0.49, 0.55, 0.62, 0.69]
vout_12324 = [vout_12324_ch1, vout_12324_ch2, vout_12324_ch3, vout_12324_ch4, vout_12324_ch5, vout_12324_ch6, vout_12324_ch7, vout_12324_ch8]

vout_12323_ch1 = [0.29, 0.36, 0.44, 0.51, 0.58, 0.65, 0.72]
vout_12323_ch2 = [0.29, 0.36, 0.44, 0.51, 0.58, 0.65, 0.72]
vout_12323_ch3 = [0.28, 0.35, 0.43, 0.50, 0.57, 0.64, 0.71]
vout_12323_ch4 = [0.28, 0.36, 0.43, 0.50, 0.57, 0.64, 0.71]
vout_12323_ch5 = [0.29, 0.36, 0.43, 0.50, 0.57, 0.64, 0.71]
vout_12323_ch6 = [0.28, 0.35, 0.42, 0.48, 0.56, 0.62, 0.69]
vout_12323_ch7 = [0.31, 0.38, 0.46, 0.53, 0.62, 0.69, 0.76]
vout_12323_ch8 = [0.29, 0.36, 0.43, 0.50, 0.58, 0.64, 0.71]
vout_12323 = [vout_12323_ch1, vout_12323_ch2, vout_12323_ch3, vout_12323_ch4, vout_12323_ch5, vout_12323_ch6, vout_12323_ch7, vout_12323_ch8]

aux_x = np.linspace(vout_pulser[0], vout_pulser[-1])
for k in range(8):
    i = str(k + 1)
    fig = plt.figure(k+2)
    fit = Linear_fit(vout_pulser, vout_12324[k])
    plt.errorbar(vout_pulser, vout_12324[k], 0.01, color="black", marker="x", ecolor="black", capsize=3, ls="", zorder=1)
    plt.xlabel(r"$V_{in}$ (V)")
    plt.ylabel(r"$V_{out}$ (V)")
    plt.title("Preamp A1422\_12324: Ch"+ i +" Gain")
    M = fit.get("slope")
    M_err = fit.get("delta_slope")
    N = fit.get("intercept")
    N_err = fit.get("delta_intercept")
    r_2 = fit.get("r_squared")
    text = "m = " + "%.3f" % M + " $\pm$ " + "%.3f" % M_err + "\n" + "n = " + "%.3f" % N + " $\pm$ " + "%.3f" % N_err + "\n" + "$r^2$ = " + "%.4f" % r_2
    plt.text(0.65, 0.74, text, transform=fig.transFigure, bbox=dict(facecolor="white"))
    plt.plot(aux_x, Linear(aux_x, M, N), "r--", zorder=0)
#
for k in range(8):
    i = str(k + 1)
    fig = plt.figure(k+10)
    fit = Linear_fit(vout_pulser, vout_12323[k])
    plt.errorbar(vout_pulser, vout_12323[k], 0.01, color="black", marker="x", ecolor="black", capsize=3, ls="", zorder=1)
    plt.xlabel(r"$V_{in}$ (V)")
    plt.ylabel(r"$V_{out}$ (V)")
    plt.title("Preamp A1422\_12323: Ch"+ i +" Gain")
    M = fit.get("slope")
    M_err = fit.get("delta_slope")
    N = fit.get("intercept")
    N_err = fit.get("delta_intercept")
    r_2 = fit.get("r_squared")
    text = "m = " + "%.3f" % M + " $\pm$ " + "%.3f" % M_err + "\n" + "n = " + "%.3f" % N + " $\pm$ " + "%.3f" % N_err + "\n" + "$r^2$ = " + "%.4f" % r_2
    plt.text(0.65, 0.74, text, transform=fig.transFigure, bbox=dict(facecolor="white"))
    plt.plot(aux_x, Linear(aux_x, M, N), "r--", zorder=0)

plt.show()

##### DECAY TIME, TODAS LAS MAGNITUDES EN MICROSEGUNDOS ####

# tau_in = [1, 10, 40, 100, 400, 1000, 3000]
# decay_in = np.log(9)*np.array(tau_in)
# decay_out = [2.1, 18.5, 47, 75, 115, 129, 143]
# tau_out = np.array(decay_out)/np.log(9)
# error_out = [0.2, 0.5, 2, 3, 3, 6, 6]
# rise_in = [7, 10, 25, 50, 80]
# rise_out = [13.5, 13.7, 17.2, 38, 76]
# error_out2 = [0.5, 0.6, 0.8, 1.5, 3]
#
# def func(x, a, b, c, d, e, f):
#     return (a*x**2+b*x+c)/(d*x**2+e*x+f)
#
# def func2(x, a, b, c):
#     return (a*x**b+c)
#
# fit = scipy.optimize.curve_fit(func, decay_in, decay_out, [1,0,1,0,1,0])
# fit2 = scipy.optimize.curve_fit(func2, rise_in, rise_out, [1,0,1])
# opt_param = fit[0]
# opt_param2 = fit2[0]
#
# plt.figure()
# plt.plot(np.linspace(0, 7000), func(np.linspace(0, 7000), *opt_param), "k--", zorder=0, linewidth=2)
# # plt.plot(decay_in, decay_out, "kx", zorder=1)
# plt.errorbar(decay_in, decay_out, error_out, color="black", marker="x", ecolor="black", capsize=3, ls="", zorder=1)
# plt.axhline(y=145, color="tab:red", linestyle="--")
# # plt.plot(tau_in, tau_out)
# # plt.loglog()
# plt.text(5500, 150, "$t=145\ \mu$s", color="tab:red")
# plt.xlabel("Decay time in ($\mu$s)")
# plt.ylabel("Decay time out ($\mu$s)")
# plt.xlim(-100)
# plt.ylim(-5,165)
# # plt.title("Preamp A1422 Timing")
#
# plt.figure()
# plt.plot(np.linspace(0, 85), func2(np.linspace(0, 85), *opt_param2), "k--", zorder=0, linewidth=2)
# # plt.plot(decay_in, decay_out, "kx", zorder=1)
# plt.errorbar(rise_in, rise_out, error_out2, color="black", marker="x", ecolor="black", capsize=3, ls="", zorder=1)
# # plt.plot(tau_in, tau_out)
# # plt.loglog()
# plt.axhline(y=13, color="tab:red", linestyle="--")
# plt.text(70, 15, "$t=13$ ns", color="tab:red")
# plt.xlabel("Rise time in (ns)")
# plt.ylabel("Rise time out (ns)")
# plt.xlim(0)
# # plt.ylim(-5,165)
# # plt.title("Preamp A1422 Timing")
# plt.show()