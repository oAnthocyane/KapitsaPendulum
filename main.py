import numpy as np
from kapitza_pendulum import Pendulum, AmplitudePendulum
from plots import PendulumPlot, AmplitudePlot

MASS = 0.1
LENGTH = 0.2
g_CONST = 9.81
AMPLITUDE = 0.1
FREQUENCY = 1.5*np.sqrt(g_CONST / LENGTH)
START_ANGLE_SPEED = 0
TIME = np.linspace(0, 9.5, 1000)
START_DEVIATION_ANGLE = np.pi / 4
START_DEVIATION_ANGLE_AMPL = np.pi - 0.1
TIME_AMPL = np.linspace(0, 50, 5000)
FREQUENCIES_AMPL = np.linspace(0.1, 3.0, 30)

pendulum = Pendulum(MASS, LENGTH, g_CONST, AMPLITUDE, FREQUENCY, [START_DEVIATION_ANGLE, START_ANGLE_SPEED], TIME)
pendulum.solve()
plot_energy = PendulumPlot(pendulum)
plot_energy.plot()
pendulum_amplitude = AmplitudePendulum(MASS, LENGTH, g_CONST, [START_DEVIATION_ANGLE_AMPL, START_ANGLE_SPEED])
plot_amplitude = AmplitudePlot(pendulum_amplitude, TIME_AMPL, FREQUENCIES_AMPL)
plot_amplitude.plot()
