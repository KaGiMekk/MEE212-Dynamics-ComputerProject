import numpy as np
from scipy.integrate import solve_ivp
from Module.shot_velocity import final_velocity

def shot_simulation(T_range, equations_of_motion, t_span, y0, m):
    theta_shot = []
    v_shot = []

    for T in T_range:
        sol = solve_ivp(equations_of_motion, t_span, y0, args=(T, m), t_eval=np.linspace(t_span[0], t_span[1], 100), rtol=1e-8, atol=1e-8)
        
        R_final = sol.y[0, -1]
        R_dot_final = sol.y[1, -1]
        theta_dot_final = sol.y[3, -1]
        
        theta_shot.append(sol.y[2, -1])
        v_shot.append(final_velocity(R_final, R_dot_final, theta_dot_final))

    return np.array(theta_shot), np.array(v_shot)
