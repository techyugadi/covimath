from math import exp
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)


class SIS:
    
    def __init__(self, N, lam, mu, gamma, S0, I0, tau):
        logger.info('Intializing SIS model ...')
        self.N = N # Total population (assumed constant)
        self.lam = lam # Daily contact rate (for adequate contact)
        self.mu = mu # Proportionality constant of daily deaths (in each class)
        self.gamma = gamma # Proportionality constant of daily recovery
        self.S0 = S0 # Initial susceptible poopulation as fraction of N
        self.I0 = I0 # Initial infected population as fraction of N
        self.tau = tau # Time window in days over which to model
        self.sigma = lam * 1.0 / (gamma + mu) # contact number
    
    # Closed form function : Infected population
    def i(self, t):
        lam = self.lam
        gamma = self.gamma
        mu = self.mu
        sigma = self.sigma
        I0 = self.I0
        
        if sigma == 1:
            return 1.0 / (lam*t + 1.0/I0)
        else:
            num = exp((gamma + mu)*(sigma -1 )*t)
            den = (exp((gamma + mu)*(sigma -1 )*t)) * (sigma * 1.0 / 
                                                (sigma - 1)) + 1.0 / I0
            
            return num * 1.0 / den
    
    # Closed form function : Susceptibile poputation
    def s(self, t):
        return 1.0 - self.i(t)
    
    def plot(self):
        logger.info('Plotting SIS model ...')
        T = np.linspace(0, self.tau, self.tau)
        I = [self.i(tim) for tim in T]
        S = [self.s(tim) for tim in T]
        
        Iarr = np.array(I)
        Sarr = np.array(S)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(T, Sarr, label='Susceptible Fraction')
        ax.plot(T, Iarr, label='Infected Fraction')
        ax.set_xlabel('Days')
        ax.set_ylabel('Fraction of Population')
        ax.set_ylim(0, 1.1)
        legend = ax.legend()
        
        plt.show()
        
if __name__ == "__main__":

    model = SIS(N=1000, lam=0.05, mu = 0.15, 
                gamma=1./10, S0=999, I0=1, tau=150)
    
    print(model.i(20))
    print(model.s(20))
    
    model.plot()
        


