import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplpub
from dynasor.tools.acfs import smoothing_function
from ase.units import kB
mplpub.setup(template='acs')

# parameters
P = 1
size = 8
cell_type = 'tric'
run_index = 0

dump_interval = 500
num_steps = 200

T_max = 1200
T_min = 1


# more
window_size1 = 2000
energy_reference = -2.0470602766055235

# read cooling data
tag = f'cooling_{cell_type}_Tstart{T_max}_Tstop{T_min}_P0_size{size}_nsteps{num_steps}_dump{dump_interval}_run-{run_index:03d}'
df1 = pd.read_csv(f'data/df_{tag}.csv')

# read heating data
tag = f'heating_{cell_type}_Tstart{T_min}_Tstop{T_max}_P0_size{size}_nsteps{num_steps}_dump{dump_interval}_run-{run_index:03d}'
df2 = pd.read_csv(f'data/df_{tag}.csv')





# process data
num_data = num_steps * 1000000 // dump_interval
df2['temp_lin'] = np.linspace(T_min, T_max, num_data)[0:len(df2)]
df1['temp_lin'] = np.linspace(T_max, T_min, num_data)[0:len(df1)]

df1['Epot'] = 1000 * (df1.Epot - energy_reference - 1.5 * kB * df1.temp_lin)
df2['Epot'] = 1000 * (df2.Epot - energy_reference - 1.5 * kB * df2.temp_lin)


# heat capacity
p = 200
window_size2 = 4 * window_size1
df1['heat_capacity'] = df1.Epot.diff(periods=p) / df1.temp_lin.diff(periods=p) / kB / 1.5 / 1000
df1['heat_capacity'] = smoothing_function(df1['heat_capacity'] + 1.0, window_size2)

df2['heat_capacity'] = df2.Epot.diff(periods=p) / df2.temp_lin.diff(periods=p) / kB / 1.5 / 1000
df2['heat_capacity'] = smoothing_function(df2['heat_capacity'] + 1.0, window_size2)


print(df1)
print(df2)

# smooth data
dt = np.diff(df1.time)[0]
print(f'smooth window {window_size1*dt} ps')
print(f'smooth window {window_size1 / len(df1) * (df1.temp.max()-df1.temp.min())} Kelvin')
keys = ['temp', 'Epot', 'alat', 'blat', 'clat', 'Mx', 'My', 'Mz', 'Rx', 'Ry', 'Rz']
for key in keys:
    df1[key] = smoothing_function(df1[key], window_size1, window_type='boxcar')
    df2[key] = smoothing_function(df2[key], window_size1, window_type='boxcar')

# plot params
col1 = 'tab:blue'
col2 = 'tab:red'
lw1 = 1.0
lw2 = 2.0
alpha1 = 1.0
alpha2 = 0.3
xlim = sorted([T_min, T_max])

# plot setup
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(4.0, 8.0), dpi=200, sharex=True)


# plot


ax1.plot(df2.temp_lin, df2.alat, '-', lw=lw2, color=col2, alpha=alpha2, label='Heating')
ax1.plot(df2.temp_lin, df2.blat, '-', lw=lw2, color=col2, alpha=alpha2)
ax1.plot(df2.temp_lin, df2.clat, '-', lw=lw2, color=col2, alpha=alpha2)
ax1.annotate('text', (-0.1, 1), fontsize = 12)

ax1.plot(df1.temp_lin, df1.alat, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1, label='Cooling')
ax1.plot(df1.temp_lin, df1.blat, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)
ax1.plot(df1.temp_lin, df1.clat, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)

ax2.plot(df2.temp_lin, df2.Mx, '-', lw=lw2, color=col2, alpha=alpha2)
ax2.plot(df2.temp_lin, df2.My, '-', lw=lw2, color=col2, alpha=alpha2)
ax2.plot(df2.temp_lin, df2.Mz, '-', lw=lw2, color=col2, alpha=alpha2)
#ax2.text(-0.1, 0 , 'b)')

ax2.plot(df1.temp_lin, df1.Mx, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)
ax2.plot(df1.temp_lin, df1.My, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)
ax2.plot(df1.temp_lin, df1.Mz, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)

ax3.plot(df2.temp_lin, df2.Rx, '-', lw=lw2, color=col2, alpha=alpha2)
ax3.plot(df2.temp_lin, df2.Ry, '-', lw=lw2, color=col2, alpha=alpha2)
ax3.plot(df2.temp_lin, df2.Rz, '-', lw=lw2, color=col2, alpha=alpha2)
#ax3.text(-0.1, 0 , 'c)')

ax3.plot(df1.temp_lin, df1.Rx, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)
ax3.plot(df1.temp_lin, df1.Ry, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)
ax3.plot(df1.temp_lin, df1.Rz, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)

ax4.plot(df2.temp_lin, df2.Epot, '-', lw=lw2, color=col2, alpha=alpha2)
ax4.plot(df1.temp_lin, df1.Epot, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)
#ax4.text(-0.1, 0 , 'd)')

ax5.plot(df2.temp_lin, df2.heat_capacity, '-', lw=lw2, color=col2, alpha=alpha2)
ax5.plot(df1.temp_lin, df1.heat_capacity, linestyle = 'dotted', lw=lw1, color=col1, alpha=alpha1)



ax1.legend(loc=4, frameon=True, framealpha=0.6, edgecolor='none')
ax1.set_xlim(xlim)
ax1.set_ylabel('Lattice params. (Å)', fontsize = 8)
ax2.set_ylabel('$Q_M$', fontsize = 8)
ax3.set_ylabel('$Q_R$', fontsize = 8)
ax4.set_ylabel('$U$ (meV/atom)', fontsize = 8)
ax5.set_ylabel('$C_p$ ($k_B$)', fontsize = 8)

ax5.set_xlabel('Temperature (K)', fontsize = 8)




ax1.set_yticks([ 4.95, 5.0, 5.05, 5.10])
ax2.set_yticks([0.0, 0.2, 0.4])
ax2.set_ylim(-0.09, 0.6)
ax3.set_ylim(-0.09, 0.6)
ax4.set_yticks([0, 5, 10, 15])
#ax5.set_yticks([1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
ax5.set_yticks([1.0, 1.5])

ax1.text(-0.15, 1, 'a)', transform=ax1.transAxes, fontsize = 8)
ax2.text(-0.15, 0.98, 'b)', transform=ax2.transAxes, fontsize = 8)
ax3.text(-0.15, 1, 'c)', transform=ax3.transAxes, fontsize = 8)
ax4.text(-0.15, 1, 'd)', transform=ax4.transAxes, fontsize = 8)
ax5.text(-0.15, 1, 'e)', transform=ax5.transAxes, fontsize = 8)

ax1.set_xlim([0, 1000])

fig.align_ylabels()
fig.subplots_adjust(hspace=0)
#fig.tight_layout()
#fig.savefig(f'figs/BZS_heating_cooling_v1.png', bbox_inches = 'tight')
fig.savefig(f'figs/BZS_heating_cooling.png', bbox_inches = 'tight')
#plt.show()
