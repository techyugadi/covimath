from math import exp
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)


class SIS:
    
    def __init__(self, N, lam, mu, gamma, I0, tau):
        logger.info('Intializing SIS model ...')
        self.N = N # Total population (assumed constant)
        self.lam = lam # Daily contact rate (for adequate contact)
        self.mu = mu # Proportionality constant of daily deaths (in each class)
        self.gamma = gamma # Proportionality constant of daily recovery
        self.I0 = I0 # Initial infected population (number, not fraction)
        self.S0 = N - I0 # Initial susceptible population (number, not fraction)
        self.tau = tau # Time window in days over which to model
        self.sigma = lam * 1.0 / (gamma + mu) # contact number
    
    # Closed form function : Infected population (fraction)
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
    
    # Infected population (absolute number)
    def iabs(self, t):
        return self.i(t) * self.N
    
    # Closed form function : Susceptibile poputation (fraction)
    def s(self, t):
        return 1.0 - self.i(t)
    
    # Susceptible population (absolute number)
    def sabs(self, t):
        return self.s(t) * self.N
    
    def plot(self, absolute=False):
        logger.info('Plotting SIS model ...')
        T = np.linspace(0, self.tau, self.tau)
        N = self.N
        
        if absolute:
            I = [self.iabs(tim) for tim in T]
            S = [self.sabs(tim) for tim in T]
        else:
            I = [self.i(tim) for tim in T]
            S = [self.s(tim) for tim in T]
        
        Iarr = np.array(I)
        Sarr = np.array(S)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        if absolute:
            slab = 'Susceptible Population'
            ilab = 'Infected Population'
        else:
            slab = 'Susceptible Fraction'
            ilab = 'Infected Fraction'
            
        ax.plot(T, Sarr, label=slab)
        ax.plot(T, Iarr, label=ilab)
        
        ax.set_xlabel('Days')
        if absolute:
            ax.set_ylabel('Number of People')
            ax.set_ylim(0, N+100)
        else:
            ax.set_ylabel('Fraction of Population')
            ax.set_ylim(0, 1.1)
            
        legend = ax.legend()
        
        plt.show()
        
if __name__ == "__main__":

    model = SIS(N=1000, lam=0.05, mu = 0.15, 
                gamma=1./10, I0=1, tau=30)
    
    print(model.i(20))
    print(model.s(20))
    
    model.plot(absolute=True)
        


