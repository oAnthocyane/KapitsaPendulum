import numpy as np


class Pendulum:

    def __init__(self, m, l, g, delta, gamma, omega_mult, state0):
        self.m = m
        self.l = l
        self.g = g
        self.delta = delta
        self.gamma = gamma
        self.omega = omega_mult * np.sqrt(g / l)
        self.state0 = state0

    def state_eqn(self, y, t):
        x, dx = y
        dydt = [dx, -self.delta*dx - np.sin(x) + self.gamma*np.cos(self.omega*t)/(self.m*self.l)]
        return dydt

    def kinetic_energy(self, dx):
        return 0.5*self.m*self.l**2*dx**2

    def potential_energy(self, x):
        return self.m*self.g*self.l*(1-np.cos(x))


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
