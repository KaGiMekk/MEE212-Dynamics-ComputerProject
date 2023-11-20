import numpy as np

def final_velocity(R, R_dot, theta_dot):
    return np.sqrt(R_dot**2 + (R**2 * theta_dot**2))
