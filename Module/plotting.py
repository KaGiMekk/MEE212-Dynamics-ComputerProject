import matplotlib.pyplot as plt
import numpy as np

def plot_radial_and_angular_position(sol):
    R_sol = sol.y[0]
    theta_sol = sol.y[2]

    # Plot R(t) and theta(t) vs. time
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    ax1.plot(sol.t, R_sol, label='R(t)')
    ax1.set_title('Radial Position R(t) vs. Time')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Radial Position R (m)')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(sol.t, theta_sol, label='theta(t)')
    ax2.set_title('Angular Position theta(t) vs. Time')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Angular Position theta (rad)')
    ax2.legend()
    ax2.grid(True)

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

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta_sol, R_sol)
    ax.set_title('Polar Plot R(theta)')
    plt.show()

def plot_theta_shot_vs_T_and_v_shot_vs_T(T_range, theta_shot, v_shot):
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
    Plots radial and angular positions as functions of time, and theta_shot and v_shot as functions of T,
    all in one figure.
    
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
    fig = plt.figure(figsize=(14, 10))
    
    # Radial Position vs. Time
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.plot(sol.t, R_sol, label='R(t)')
    ax1.set_title('Radial Position R(t) vs. Time')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Radial Position R (m)')
    ax1.legend()
    ax1.grid()
    
    # Angular Position vs. Time
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.plot(sol.t, theta_sol, label='theta(t)')
    ax2.set_title('Angular Position theta(t) vs. Time')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Angular Position theta (rad)')
    ax2.legend()
    ax2.grid()
    
    # Polar Plot
    ax3 = fig.add_subplot(2, 3, 3, projection='polar')
    ax3.plot(theta_grid, R_grid)
    ax3.set_title('Polar Plot of R(theta)')
    ax3.grid(True)
    
    # Theta_shot vs. Tension T
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.plot(T_range, theta_shot, 'b')
    ax4.set_title('Theta_shot vs. Torque T')
    ax4.set_xlabel('Torque T (Nm)')
    ax4.set_ylabel('Theta_shot (rad)')
    ax4.grid()
    
    # V_shot vs. Tension T
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.plot(T_range, v_shot, 'r')
    ax5.set_title('V_shot vs. Torque T')
    ax5.set_xlabel('Torque T (Nm)')
    ax5.set_ylabel('V_shot (m/s)')
    ax5.grid()
    
    plt.tight_layout()
    plt.show()
