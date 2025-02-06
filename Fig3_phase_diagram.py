import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplpub
mplpub.setup(template='acs')
#import matplotlib
#matplotlib.rcParams.update({'font.size': 52})

# read data
df1 = pd.read_csv('data/ortho_tetra_Tc_vals_from_heating.csv')
df2 = pd.read_csv('data/tetra_cubic_Tc_vals_from_heating.csv')

# fit lines
params1 = np.polyfit(df1.pressure, df1.temperature, deg=3)
params2 = np.polyfit(df2.pressure, df2.temperature, deg=2)


# plot setup
fig = plt.figure(figsize=(3.4, 2.8), dpi=200)
ax1 = fig.add_subplot(111)

# plot params
col1 = 'k'
col2 = 'k'

xlim = [-4, 10]
ylim = [0, 1200]
x_lin = np.linspace(*xlim, 10000)
# MD results 
ax1.plot(df1.temperature,df1.pressure,  'o', markersize = 3, color=col1)
ax1.plot(df2.temperature,df2.pressure,  'o', markersize = 3, color=col2)

#Jaykhedkar et al
#ax1.plot(773, 0,'k^', color = 'k', fillstyle = 'none')

#Jaiswal et al
#ax1.plot(670, 0,'x', color = 'k', fillstyle = 'none')

# Gross et al
x_values = [300, 300]
y_values = [0, 8.9]
#ax1.plot(x_values, y_values, 'k_', linestyle = '--')
# Ye et al
y_values1 = [0, 0] 
x_values1 = [10, 875]
#ax1.plot(x_values1, y_values1, 'k_', linestyle = ':')


y_lin1 = np.polyval(params1, x_lin)
y_lin2 = np.polyval(params2, x_lin)
ax1.plot(y_lin1, x_lin, '-k', color=col1)
ax1.plot(y_lin2, x_lin, '-k', color=col2)
#
ax1.fill_betweenx(x_lin,y_lin1, -1, color='tab:red', alpha=0.2)
ax1.fill_betweenx(x_lin,y_lin1, y_lin2, color='tab:blue', alpha=0.2)
ax1.fill_betweenx(x_lin,100000, y_lin2, color='gold', alpha=0.2)
#
ax1.set_xlim(ylim)
ax1.set_ylim(xlim)
ax1.set_ylabel('Pressure (GPa)')
ax1.set_xlabel('Temperature (K)')
#
## mark regions
ax1.text(0.7, 0.1, r'Cubic $\UG{Pm\overline{3}m}$', transform=ax1.transAxes, fontsize = 7)
ax1.text(0.64, 0.78, r'Tetragonal $\UG{I4/mcm}$', transform=ax1.transAxes, fontsize = 7)
ax1.text(0.08, 0.5, r'Orthorhombic $\UG{Pnma}$', transform=ax1.transAxes, fontsize = 7)
#
#fig.tight_layout()
plt.savefig('data/phase_diagram.png', bbox_inches = 'tight')
#plt.show()

