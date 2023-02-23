# -*- coding: utf-8 -*-
"""
Use FE-SAFE fatigue analysis output to create a Goodman diagram plot.

Created on Tue Sep 29 09:30:24 2020

@author: tvj
"""

import numpy as np
import matplotlib.pyplot as plt

filename = 'LCU_221128_dynamic_mesh_FESAFE'

SultT = 356.E+6   # Ultimate tensile strength of irradiated tungsten [Pa]
SultC = 1000.E+6  # Ultimate compressive strength of irradiated tungsten [Pa]

#-------------------------------------------------------------
# Calculate fatigue strength of irradiated tungsten
# See <tungstenFatigue-Irradiated-Rev2.ipynb>
#-------------------------------------------------------------
Life = 10.0 # years
Year_to_Sec = 365.0*24.0*3600.0 # sec in a year
Uptime = 5000.0 / (365.0*24.0) # hours operation / year
PulseFreq = 15.0 # pulses / sec
NumTarget = 21.0
Pulses = Life * Year_to_Sec * Uptime * PulseFreq / NumTarget

Sfprime = SultT
b = -0.04150804

Slife = Sfprime * (2 * Pulses)**b

#-------------------------------------------------------------



"""
LOAD DATA FROM FE-SAFE POSTPROCESSING
===============================================================================
FE-SAFE can produce a history text file with the Haigh diagram.  Must first
clean up this file as follows:
  * cat FESAFE.odb-history.txt | grep -n 'El#' > grepout
  * head grepout
  * vi FESAFE.odb-history.txt
  * <line number> <shift+g>
  * <ma>
  * <ctrl+end>
  * <d'a>
  * <:wq>
  * mv FESAFE.odb-history.txt FESAFE.txt
"""

Sm, Sa = np.loadtxt(filename+".txt", skiprows=7, unpack=True)
Smean = Sm*1.E+6
Samp = Sa*1.E+6




"""
CALCULATE FACTORS OF SAFETY
===============================================================================
"""

def GoodmanSamp(SultC,SultT,Slife,Smean):
    if Smean >= -1*SultC and Smean < Slife-SultC:
        Samp = SultC * (1 - abs(Smean)/SultC)
    elif Smean >= Slife-SultC and Smean < 0:
        Samp = Slife
    elif Smean >= 0 and Smean <= SultT:
        Samp = Slife * (1 - Smean/SultT)
    else:
        Samp = 0  
    return Samp


def getFOS(SultC,SultT,Slife,Smean,Samp):
    
    if Smean >= -1*SultC and Smean < Slife-SultC:
        FOS = 1 / (Samp/SultC + abs(Smean)/SultC)
    elif Smean >= Slife-SultC and Smean < 0:
        FOS = Slife / Samp
    elif Smean >= 0 and Smean <= SultT:
        FOS = 1 / (Samp/Slife + abs(Smean)/SultT)
    else:
        FOS = 0  
    
    return FOS

FOS = np.empty_like(Smean)
for i in range(len(FOS)):
    FOS[i] = getFOS(SultC,SultT,Slife,Smean[i],Samp[i])


# Get the smallest, overall FOS
Goodman_FOS = FOS.min()
print("The minimum fatigue factor of safety is:")
print(Goodman_FOS)







"""
CALCULATE GOODMAN RELATIONSHIP
===============================================================================
"""

# Initialize data points for Smith diagram
Goodman_Smean = np.array([-1*SultC, -1*SultC+Slife, 0, SultT])
Goodman_Samp = np.zeros(len(Goodman_Smean))

# Initialize data points for Smith diagram w/ FOS
Goodman_Smean_FOS = Goodman_Smean / Goodman_FOS
Goodman_Samp_FOS = np.zeros(len(Goodman_Smean_FOS))

for item in range(len(Goodman_Smean)):
    Goodman_Samp[item] = GoodmanSamp(SultC,
                                     SultT,
                                     Slife,
                                     Goodman_Smean[item])
    
    Goodman_Samp_FOS[item] = GoodmanSamp(SultC/Goodman_FOS,
                                         SultT/Goodman_FOS,
                                         Slife/Goodman_FOS,
                                         Goodman_Smean_FOS[item])



"""
PLOT GOODMAN DIAGRAM
===============================================================================
"""
fig2 = plt.figure(figsize=(6,6), dpi=200)
ax2 = fig2.add_axes([0,0,1,1])

ax2.plot(Goodman_Smean/1.E6,
        Goodman_Samp/1.E6,
        color='blue',
        label="Goodman")
ax2.plot(Goodman_Smean_FOS/1.E6,
        Goodman_Samp_FOS/1.E6,
        color='blue',
        ls='--',
        label=("{:.2f}".format(Goodman_FOS)+' FOS'))
ax2.set_xlabel('Mean Stress [MPa]')
ax2.set_ylabel('Stress Amplitude [MPa]')
ax2.set_title(filename)


# OVERLAY THE FESAFE results

ax2.plot(Smean/1.E6, 
         Samp/1.E6, 
         color='red',
         marker='.',
         lw=0,
         label="Critical Plane")

plt.legend(loc='upper right')
plt.grid(which='major', axis='both')

fig2.savefig(filename+'_Goodman.png', bbox_inches = "tight")
