import numpy as np
	import matplotlib.pyplot as plt
	from scipy.integrate import solve_ivp
		
	a, b, c = 0.2, 0.2, 5.7
		
	def rossler(t, state):
		x, y, z = state
		return [
			-y - z,
			x + a*y,
			b + z*(x - c)
		]
		
	t_span = (0, 100)
	t_eval = np.linspace(0, 100, 5000)
	
	x0_1 = [1.0, 1.0, 1.0]
	x0_2 = [1.000001, 1.0, 1.0]  # small perturbation
		
	sol1 = solve_ivp(rossler, t_span, x0_1, t_eval=t_eval)
	sol2 = solve_ivp(rossler, t_span, x0_2, t_eval=t_eval)
		
	# Euclidean distance
	dist = np.linalg.norm(sol1.y - sol2.y, axis=0)
		
	plt.figure()
	plt.plot(t_eval, dist, color='black')
	plt.xlabel("Time")
	plt.ylabel("Distance")
	plt.yscale("log")
	plt.grid()
	
	plt.show()