#Calculate Observables for BB84 protocol

import numpy as np

class BB84:

    def __init__(self,channel,detector):
        self.channel=channel
        self.detector=detector


    def GetObservables(self,mu,L):   #Calculate protocol observables
        #Calculate required parameters
        T=self.channel.GetTransmittance(L)
        p_dark=self.detector.darkCount
        e_det=self.detector.errorRate
        eta=self.detector.GetEta(T)
        e0=0.5
        
        Q_mu=1-(1-p_dark)**2*np.exp(-mu*eta)  #Total gain for protocol per pulse

        ErrorGain={
            "Z": (1-p_dark)*(np.exp(-mu*eta*(1-e_det["Z"]))-np.exp(-mu*eta*e_det["Z"]))
            "X": (1-p_dark)*(np.exp(-mu*eta*(1-e_det["X"]))-np.exp(-mu*eta*e_det["X"]))
        }

        E_mu={
            "Z":0.5+ErrorGain["Z"]/(2*Q_mu),
            "X" :0.5+ErrorGain["X"]/(2*Q_mu)
        }


        return {"Q_mu" :Q_mu,
                "ErrorGain": ErrorGain,
                "QBER": E_mu}
