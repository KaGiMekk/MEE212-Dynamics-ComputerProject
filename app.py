import numpy as np
from Module.plotting import *
from Module.Solve_equation import *
from Module.shot_simulation import *

# Constants
m = 1  # mass of the collar
T = 1  # torque in the rod
R0 = 0.1  # initial radial position in meters
theta0 = 0  # initial angle in radians
theta_dot0 = 0  # initial angular velocity
R_dot0 = 0  # initial radial velocity
T_range = np.linspace(0, 3, 100) # Range of tension T from 0 to 3 Nm

if __name__ == '__main__':

    # Time span for the solution
    t_span = [0, 1]
    t_eval = np.linspace(t_span[0], t_span[1], 100)

    y0 = [R0, R_dot0, theta0, theta_dot0]

    # Solve the differential equations
    sol = solve_equations(equations_of_motion, t_span, y0, t_eval, T, m)
    
    # Run the simulation for each value of T
    theta_shot, v_shot = shot_simulation(T_range, equations_of_motion, t_span, y0, m)

    # Plot the results
    # plot_radial_and_angular_position(sol)
    # plot_polar(sol)

    # Plot the results
    # plot_theta_shot_vs_T_and_v_shot_vs_T(T_range, theta_shot, v_shot)

    plot_all_in_one_figure(sol, T_range, theta_shot, v_shot)