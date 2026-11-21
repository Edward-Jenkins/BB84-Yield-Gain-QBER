#Characteristics for photon threshold detector
import numpy as np

class Detector:

    def __init__(self,eta_det,T_det,p_dark,e_det):
        self.detectorEfficiency=eta_det
        self.internalTransmittance=T_det
        self.darkCount=p_dark
        self.errorRate=e_det


    def GetEta(self,T):       #Total detection efficiency for photon travelling from Alice to Bob
     eta=self.detectorEfficiency*self.internalTransmittance*T
     return eta