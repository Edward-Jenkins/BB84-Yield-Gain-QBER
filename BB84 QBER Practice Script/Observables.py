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
        
        Q_mu=p_dark+1-np.exp(-eta*mu)  #Total gain for protocol per pulse

        ErrorGain={
            "Z": e0*p_dark+e_det["Z"]*(1-np.exp(-eta*mu)),
            "X": e0*p_dark+e_det["X"]*(1-np.exp(-eta*mu))
        }

        E_mu={
            "Z":ErrorGain["Z"]/Q_mu,
            "X" :ErrorGain["X"]/Q_mu
        }


        return {"Q_mu" :Q_mu,
                "ErrorGain": ErrorGain,
                "QBER": E_mu}
