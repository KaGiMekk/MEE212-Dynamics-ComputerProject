import numpy as np
from Module.plotting import *
from Module.Solve_equation import *

# Constants
m = 1  # mass of the collar
T = 1  # tension in the rod
R0 = 0.1  # initial radial position in meters
theta0 = 0  # initial angle in radians
theta_dot0 = 0  # initial angular velocity
R_dot0 = 0  # initial radial velocity

# Time span for the solution
t_span = [0, 1]
t_eval = np.linspace(t_span[0], t_span[1], 100)

y0 = [R0, R_dot0, theta0, theta_dot0]

# Solve the differential equations
sol = solve_equations(equations_of_motion, t_span, y0, t_eval, T, m)

# Plot the results
plot_radial_and_angular_position(sol)
plot_polar(sol)