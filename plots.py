
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class PendulumPlot:

    def __init__(self, pendulum):
        self.pendulum = pendulum

    def plot(self):
        plt.plot(self.pendulum.t, self.pendulum.kinetic, label='Кинетическая')
        plt.plot(self.pendulum.t, self.pendulum.potential, label='Потенциальная')
        plt.xticks(np.arange(1, 10, 2))
        plt.title('Energy vs time')
        plt.savefig('energy_time.png')
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