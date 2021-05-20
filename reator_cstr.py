import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

q = 3 #L/s
cae = 2 #mol/L
V = 20 #L
Te = 350 #K
rho = 1000 #g/L
Cp = 1.9 #J/(g.K)
deltaH = 50000 #J/mol  (-DeltaH)
E_R = 8750 #K (E/R)
k0 = 0.0029 #L/mol.min
UA = 50000 #J/(min.K)
Tc = 100 #K

#condicoes iniciais
ca0 = 3.27 #mol/L
T0 = 350 #K


def funcaoCSTR(y,t):
    T, Ca = y
    k = k0*np.exp(-E_R/T)
    dT_dt = (rho*q*Cp*(Te-T) + UA*(Tc-T) + deltaH*V*k*Ca)/(V*rho*Cp) #balanco de energia
    dCa_dt = (q*(cae-Ca) - V*k*Ca)/V #balanco de massa
    return [dT_dt, dCa_dt]

t = np.linspace(0, 30, num=100)
y = odeint(funcaoCSTR, [T0, ca0], t)

T_vetor = y[:,0]
Ca_vetor = y[:,1]

plt.plot(t, T_vetor)

plt.plot(t, Ca_vetor)
