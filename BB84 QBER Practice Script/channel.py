#Characteristics for fibre channel
import numpy as np

class FibreChannel:

    def __init__(self,alpha):
        self.lossCoefficient = alpha


    def GetTransmittance(self,L):
        #Calculates transmission over length L of fibre using Beer Lambert Law

        T=10**(-(self.lossCoefficient*L)/10)
        return T