
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class PendulumPlot:

    def __init__(self, pendulum, t):
        self.pendulum = pendulum
        self.t = t
        self.solution = odeint(self.pendulum.state_eqn, self.pendulum.state0, self.t)

    def energy_plot(self):
        kinetic_energy = self.pendulum.kinetic_energy(self.solution[:, 1])
        potential_energy = self.pendulum.potential_energy(self.solution[:, 0])

        plt.figure()
        plt.plot(self.t, kinetic_energy, label='Kinetic Energy')
        plt.plot(self.t, potential_energy, label='Potential Energy')
        plt.xlabel('t')
        plt.ylabel('Energy')
        plt.title('Energy vs time')
        plt.legend()
        plt.savefig('energy-time.png')
        plt.show()


class AmplitudePlot:

    def __init__(self, pendulum, t, frequencies):
        self.pendulum = pendulum
        self.t = t
        self.frequencies = frequencies
        self.amplitudes = self.calculate_amplitudes()

    def calculate_amplitudes(self):
        amplitudes = []
        for f in self.frequencies:
            omega = 2*np.pi*f
            solution = odeint(self.pendulum.equation, self.pendulum.y0, self.t, args=(0.1, 1.0, omega))
            amplitude = np.max(np.abs(solution[:, 0]))
            amplitudes.append(amplitude)
        return amplitudes

    def plot(self):
        plt.figure()
        plt.plot(self.frequencies, self.amplitudes)
        plt.xlabel('Frequency (f)')
        plt.ylabel('Amplitude (a)')
        plt.title('Amplitude-Frequency Diagram')
        plt.savefig('a-f_plot.png')
        plt.grid(True)
        plt.show()