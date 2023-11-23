from scipy.integrate import solve_ivp

def equations_of_motion(t, y, T, m):
    R, R_dot, theta, theta_dot = y
    dR_ddot = R * theta_dot**2
    dtheta_ddot = ((T / R) - (2 * m * R_dot * theta_dot)) / (m * R)
    return [R_dot, dR_ddot, theta_dot, dtheta_ddot]

def solve_equations(equations, t_span, y0, t_eval, T, m):
    sol = solve_ivp(equations, t_span, y0, args=(T, m), t_eval=t_eval)
    return sol
