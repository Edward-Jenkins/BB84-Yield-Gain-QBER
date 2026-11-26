#Simple BB84 Learining Script for Yield, Gain, QBER and SKR

import numpy as np
from channel import FibreChannel
from detector import Detector
from Observables import BB84

from matplotlib import pyplot as plt
#Constants

eta_det=0.22    #Detector efficiency
T_bob=0.5   #Bobs internal transmittance
alpha=0.2   #Fibre loss coefficient
p_dark=1e-6
e_det={"Z":0.02,"X":0.03}

#Parameters

l=10    #Distance(s) between Alice and Bob
MeanPhotonNums=np.linspace(0.000000001,100,200)  #Mean photon num(s) of Alices WCP

#####################################################################################################

channel=FibreChannel(alpha)
detector=Detector(eta_det,T_bob,p_dark,e_det)
protocol=BB84(channel,detector)

Gain=[]
ErrorGain_Z=[]
ErrorGain_X=[]
QBER_Z=[]
QBER_X=[]

for mu in MeanPhotonNums:
    obs=protocol.GetObservables(mu,l)
    Gain.append(obs["Q_mu"])
    ErrorGain_Z.append(obs["ErrorGain"]["Z"])
    ErrorGain_X.append(obs["ErrorGain"]["X"])
    QBER_Z.append(obs["QBER"]["Z"])
    QBER_X.append(obs["QBER"]["X"])
    
#######################################################################################################

fig,ax = plt.subplots()
ax.set_title("Total BB84 gain vs WCP Strength")
ax.plot(MeanPhotonNums,Gain,color="orange")
ax.set_xlabel("Mean Photon Number per pulse")
ax.set_ylabel("Gain per pulse")
plt.show()
fig.savefig('Figures/Simple_Gain_vs_Mu')
plt.close(fig)

fig,ax = plt.subplots()
ax.set_title("Error Gain vs WCP Strength")
ax.plot(MeanPhotonNums,ErrorGain_Z,color="orange",label="Z Basis")
ax.plot(MeanPhotonNums,ErrorGain_X,color="black",label="X Basis")
ax.set_xlabel("Mean Photon Number per pulse")
ax.set_ylabel("Error Gain per pulse")
ax.legend()
plt.show()
fig.savefig('Figures/Simple_ErrorGain_vs_Mu')
plt.close(fig)

fig,ax = plt.subplots()
ax.set_title("QBER vs WCP Strength")
ax.plot(MeanPhotonNums,QBER_Z,color="orange",label="Z Basis")
ax.plot(MeanPhotonNums,QBER_X,color="black",label="X Basis")
ax.set_yscale('log')
ax.set_xlabel("Mean Photon Number per pulse")
ax.set_ylabel("QBER")
ax.legend()
plt.show()
fig.savefig('Figures/Simple_QBER_vs_Mu')
plt.close(fig)
######################################################################################################

distances = list(range(0, 181, 5))
mu=0.5

Gain=[]
ErrorGain_Z=[]
ErrorGain_X=[]
QBER_Z=[]
QBER_X=[]

for d in distances:
     obs=protocol.GetObservables(mu,d)
     Gain.append(obs["Q_mu"])
     ErrorGain_Z.append(obs["ErrorGain"]["Z"])
     ErrorGain_X.append(obs["ErrorGain"]["X"])
     QBER_Z.append(obs["QBER"]["Z"])
     QBER_X.append(obs["QBER"]["X"])

fig,ax = plt.subplots()
ax.set_title("Gain vs Distance")
ax.plot(distances,Gain,color="orange")
ax.set_xlabel("Distance /km")
ax.set_ylabel("Gain")
ax.set_yscale('log')
plt.show()
fig.savefig('Figures/Simple_Gain_vs_Distance')
plt.close(fig)


fig,ax = plt.subplots()
ax.set_title("QBER vs Distance")
ax.plot(distances,QBER_Z,color="orange",label="Z Basis")
ax.plot(distances,QBER_X,color="black",label="X Basis")
ax.set_xlabel("Distance /km")
ax.set_ylabel("QBER")
ax.legend()
plt.show()
fig.savefig('Figures/Simple_QBER_vs_Distance')
plt.close(fig)
