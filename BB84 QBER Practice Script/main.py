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
e_det=0.03

#Parameters

l=100    #Distance(s) between Alice and Bob
MeanPhotonNums=np.linspace(0.0001,2,100)  #Mean photon num(s) of Alices WCP


#####################################################################################################

channel=FibreChannel(alpha)
detector=Detector(eta_det,T_bob,p_dark,e_det)
protocol=BB84(channel,detector)

Gain=[]
ErrorGain=[]
QBER=[]

for mu in MeanPhotonNums:
    obs=protocol.GetObservables(mu,l)
    Gain.append(obs["Q_mu"])
    ErrorGain.append(obs["ErrorGain"])
    QBER.append(obs["QBER"])
    
print(Gain)

#######################################################################################################

fig,ax = plt.subplots()
ax.set_title("Total BB84 gain vs WCP Strength")
ax.plot(MeanPhotonNums,Gain)
ax.set_xlabel("Mean Photon Number per pulse")
ax.set_ylabel("Gain per pulse")
plt.show()

fig,ax = plt.subplots()
ax.set_title("Error Gain vs WCP Strength")
ax.plot(MeanPhotonNums,ErrorGain)
ax.set_xlabel("Mean Photon Number per pulse")
ax.set_ylabel("Error Gain per pulse")
plt.show()

fig,ax = plt.subplots()
ax.set_title("QBER vs WCP Strength")
ax.plot(MeanPhotonNums,QBER)
ax.set_xlabel("Mean Photon Number per pulse")
ax.set_ylabel("QBER")
plt.show()

######################################################################################################

distances = list(range(0, 181, 5))
mu=0.5

Gain=[]
ErrorGain=[]
QBER=[]
for d in distances:
     obs=protocol.GetObservables(mu,d)
     Gain.append(obs["Q_mu"])
     ErrorGain.append(obs["ErrorGain"])
     QBER.append(obs["QBER"])

fig,ax = plt.subplots()
ax.set_title("Gain vs Distance")
ax.plot(distances,Gain)
ax.set_xlabel("Distance /km")
ax.set_ylabel("Gain")
ax.set_yscale('log')
plt.show()


fig,ax = plt.subplots()
ax.set_title("QBER vs Distance")
ax.plot(distances,QBER)
ax.set_xlabel("Distance /km")
ax.set_ylabel("QBER")
plt.show()
