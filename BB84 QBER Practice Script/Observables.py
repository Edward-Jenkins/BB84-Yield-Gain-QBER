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
        
        Q_mu=1-(1-p_dark)*np.exp(-eta*mu)  #Total gain for protocol per pulse
        ErrorGain=e0*p_dark+e_det*(1-np.exp(-eta*mu))
        E_mu=ErrorGain/Q_mu

        return {"Q_mu" :Q_mu,
                "ErrorGain": ErrorGain,
                "QBER": E_mu}
