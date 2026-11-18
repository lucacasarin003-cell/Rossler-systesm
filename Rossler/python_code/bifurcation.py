import numpy as np
	import matplotlib.pyplot as plt
	from scipy.integrate import solve_ivp
	from scipy.signal import find_peaks
	
	def rossler(t, state, a, b, c):
		x, y, z = state
	
		dxdt = -y - z
		dydt = x + a * y
		dzdt = b + z * (x - c)
	
		return [dxdt, dydt, dzdt]
	
	
	def bifurcation(param_name, param_values, a, b, c):
	
		x_data = []
		p_data = []
	
		for i, p in enumerate(param_values):
	
			aa, bb, cc = a, b, c
	
			if param_name == "a":
				aa = p
			elif param_name == "b":
				bb = p
			elif param_name == "c":
				cc = p
	
			t0, tf = 0, 300
			t_eval = np.arange(t0, tf, 0.05)
	
			def escape_event(t, state, *args):
				if np.any(np.abs(state) > 1000):
					return 0
				return 1
	
			escape_event.terminal = True
	
			sol = solve_ivp(
				rossler,
				[t0, tf],
				[1.0, 1.0, 1.0],
				args=(aa, bb, cc),
				method="RK45",
				t_eval=t_eval,
				rtol=1e-5,
				atol=1e-7,
				events=escape_event
			)
	
			if not sol.success or (sol.t_events and 
						len(sol.t_events[0]) >	0):
				continue
	
			x = sol.y[0]
			t = sol.t
	
			mask = t > 200
			x_stable = x[mask]
	
			peaks, _ = find_peaks(x_stable)
			maxima = x_stable[peaks]
	
			if len(maxima) > 0:
				maxima = np.unique(np.round(maxima, 4))
	
				p_data.extend([p] * len(maxima))
				x_data.extend(maxima)
	
		if len(p_data) == 0:
			print(f"No stable data found for the parameter {param_name}")
	        return
	
	
		plt.figure(figsize=(11, 6))
	
		plt.scatter(
			p_data,
			x_data,
			s=0.5,
			color='black',
			alpha=0.5
		)
	
		plt.xlabel(f"Parameter {param_name}", fontsize=12)
		plt.ylabel(r"$x_{max}$", fontsize=12)
	
	
		plt.tight_layout()
		
		plt.show()
	
	
	a0, b0, c0 = 0.2, 0.2, 5.7
	
	a_values = np.linspace(0.0, 0.35, 350)
	b_values = np.linspace(0.0, 2.0, 500)
	c_values = np.linspace(1.5, 7.0, 350)
	
	bifurcation("a", a_values, a0, b0, c0)
	bifurcation("b", b_values, a0, b0, c0)
	bifurcation("c", c_values, a0, b0, c0)