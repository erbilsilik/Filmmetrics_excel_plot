# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:03:22 2016

@author: Naci EKEM
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 02:17:31 2016

@author: erbil
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:17:49 2016

@author: Erbil ŞİLİk
"""

# -*- coding: utf-8 -*-


# import modules
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib
import itertools

# Import the excel file and call it xls_file
xls_file = pd.ExcelFile('filmmetrics.xlsx')
sheet_name = xls_file.sheet_names
print (sheet_name)
marker = ["o", "s", "p", "*", "h", "+", "<"]
g = itertools.cycle(marker)

# Load the xls file's Sheet1 as a dataframe
for i in range(0, len(sheet_name)):
#    print(sheet_name[i])
    df = xls_file.parse(sheet_name[i])
    numpyMatrix = df.as_matrix()
    wave_length = numpyMatrix[:,0]
    reflection = numpyMatrix[:,1]
    refractive_index = numpyMatrix[:,2]
    rp_dielectric_cons = (refractive_index)**2 #real part of dielectric constant
    extinction_coefficient = 0
    plt.plot(wave_length, rp_dielectric_cons, label=sheet_name[i],marker = g.__next__(), 
             markevery=30)
    plt.legend(loc=1,prop={'size':10})


plt.xlabel(r'$\mathrm{Wavelength \ (nm)}$')
plt.ylabel(r'$\mathrm{Dielectric\ Constant}\ (\epsilon_r) $') 




params = {'legend.fontsize': 18,
          'axes.labelsize': 18,
          'axes.titlesize': 18,
          'xtick.labelsize' :12,
          'ytick.labelsize': 12,
          'mathtext.fontset': 'cm',
          'mathtext.rm': 'serif',
          'grid.color': 'grey',
          'grid.linestyle': '-',
          'grid.linewidth': 0.5,
         }
matplotlib.rcParams.update(params)


plt.tight_layout()
plt.grid(True)

plt.savefig('Dielectric_constant.tif', dpi=1000)
   




   
