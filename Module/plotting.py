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

def plot_theta_shot_vs_T_and_v_shot_vs_T(T_range, theta_shot, v_shot):
    # Create a figure with two subplots
    plt.figure(figsize=(12, 5))

    # First subplot for Theta_shot vs. Tension T
    plt.subplot(1, 2, 1)
    plt.plot(T_range, theta_shot, 'b')
    plt.title('Theta_shot vs. Torque T')
    plt.xlabel('Torque T (Nm)')
    plt.ylabel('Theta_shot (rad)')
    plt.grid()

    # Second subplot for V_shot vs. Tension T
    plt.subplot(1, 2, 2)
    plt.plot(T_range, v_shot, 'r')
    plt.title('V_shot vs. Torque T')
    plt.xlabel('Torque T (Nm)')
    plt.ylabel('V_shot (m/s)')
    plt.grid()

    # Show the figure
    plt.show()

def plot_all_in_one_figure(sol, T_range, theta_shot, v_shot):
    """
    Plots radial position, angular position, polar plot of radial vs angular position,
    theta_shot vs Tension T, and v_shot vs Tension T, all in one figure.
    
    Parameters:
    sol (OdeResult): The solution object returned by solve_ivp.
    T_range (array): Array of Tension T values.
    theta_shot (array): Array of Theta_shot values corresponding to T_range.
    v_shot (array): Array of V_shot values corresponding to T_range.
    """

    R_sol = sol.y[0]
    theta_sol = sol.y[2]
    theta_grid = np.linspace(0, 2 * np.pi, 100)
    R_grid = np.interp(theta_grid, theta_sol % (2 * np.pi), R_sol)

    # Create a figure with five subplots
    fig = plt.figure(figsize=(15, 12))
    
    # Radial Position vs. Time
    ax1 = fig.add_subplot(3, 2, 1)
    ax1.plot(sol.t, R_sol, label='R(t)')
    ax1.set_title('Radial Position R(t) vs. Time')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Radial Position R (m)')
    ax1.legend()
    ax1.grid()

    # Angular Position vs. Time
    ax2 = fig.add_subplot(3, 2, 2)
    ax2.plot(sol.t, theta_sol, label='theta(t)')
    ax2.set_title('Angular Position theta(t) vs. Time')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Angular Position theta (rad)')
    ax2.legend()
    ax2.grid()

    # Polar Plot
    ax3 = fig.add_subplot(3, 2, 3, projection='polar')
    ax3.plot(theta_grid, R_grid)
    ax3.set_title('Polar Plot of R(theta)')
    ax3.set_xlabel('Theta (rad)')
    ax3.set_ylabel('R (m)')
    ax3.grid(True)

    # Theta_shot vs. Tension T
    ax4 = fig.add_subplot(3, 2, 4)
    ax4.plot(T_range, theta_shot, 'b')
    ax4.set_title('Theta_shot vs. Torque T')
    ax4.set_xlabel('Torque T (Nm)')
    ax4.set_ylabel('Theta_shot (rad)')
    ax4.grid()

    # V_shot vs. Tension T
    ax5 = fig.add_subplot(3, 2, 5)
    ax5.plot(T_range, v_shot, 'r')
    ax5.set_title('V_shot vs. Torque T')
    ax5.set_xlabel('Torque T (Nm)')
    ax5.set_ylabel('V_shot (m/s)')
    ax5.grid()

    plt.tight_layout()
    plt.show()

# Example usage
# plot_all_in_one_figure(sol, T_range, theta_shot, v_shot)
