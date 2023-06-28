import numpy as np
from scipy.integrate import odeint

class Pendulum:
    def __init__(self, m, l, g, a, omega, state0, t):
        self.m = m
        self.l = l
        self.g = g
        self.a = a
        self.omega = omega
        self.state0 = state0
        self.t = t
        self.nu = np.sqrt(g / l)

    def state_eqn(self, state, t):
        phi, phidot = state
        phidotdot = -(self.a*self.omega**2*np.cos(self.omega*t) + self.g)*np.sin(phi) / self.l
        return phidot, phidotdot

    def energy(self, state, t):
        phi, phidot = state
        kinetic = 0.5*self.m*(self.l*phidot)**2 + self.m*self.a*self.omega*np.sin(self.omega*t)*self.l*phidot*np.sin(phi) + 0.5*self.m*self.a**2*self.omega**2*np.sin(self.omega*t)**2
        potential = -self.m*self.g*(self.l*np.cos(phi) + self.a*np.cos(self.omega*t))
        return kinetic, potential

    def solve(self):
        self.state = odeint(self.state_eqn, self.state0, self.t)
        self.kinetic, self.potential = np.array([self.energy(s, t) for s, t in zip(self.state, self.t)]).T



class AmplitudePendulum:

    def __init__(self, m, l, g, y0):
        self.m = m
        self.l = l
        self.g = g
        self.y0 = y0

    def equation(self, y, t, delta, gamma, omega):
        x, v = y
        dxdt = v
        dvdt = -delta*v - self.g/self.l*np.sin(x) + gamma*np.cos(omega*t)/self.m
        return [dxdt, dvdt]
