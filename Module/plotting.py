import matplotlib.pyplot as plt
import numpy as np

def plot_radial_and_angular_position(sol):
    """
    Plots the radial and angular positions as functions of time.
    
    Parameters:
    sol (OdeResult): The solution object returned by solve_ivp.
    """
    R_sol = sol.y[0]
    theta_sol = sol.y[2]

    # Plot R(t) and theta(t) vs. time
    fig, (ax1, ax2) = plt.subplots(2, figsize=(12, 10))
    ax1.plot(sol.t, R_sol, label='R(t)')
    ax1.set_title('Radial Position R(t) vs. Time')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Radial Position R (m)')
    ax1.legend()
    ax1.grid()

    ax2.plot(sol.t, theta_sol, label='theta(t)')
    ax2.set_title('Angular Position theta(t) vs. Time')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Angular Position theta (rad)')
    ax2.legend()
    ax2.grid()

    plt.tight_layout()
    plt.show()

def plot_polar(sol):
    """
    Plots the radial position as a function of angular position in polar coordinates.
    
    Parameters:
    sol (OdeResult): The solution object returned by solve_ivp.
    """
    R_sol = sol.y[0]
    theta_sol = sol.y[2]

    # Prepare for polar plot
    theta_grid = np.linspace(0, 2 * np.pi, 100)
    R_grid = np.interp(theta_grid, theta_sol % (2 * np.pi), R_sol)

    # Plot R(theta) in polar coordinates
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    ax.plot(theta_grid, R_grid)
    ax.set_title('Polar Plot of R(theta)')
    ax.set_xlabel('Theta (rad)')
    ax.set_ylabel('R (m)')
    ax.grid(True)

    plt.show()
