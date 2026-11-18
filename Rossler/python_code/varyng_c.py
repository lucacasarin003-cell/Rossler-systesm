import numpy as np
	import matplotlib.pyplot as plt
	from scipy.integrate import solve_ivp
	
	def rossler(t, state, a, b, c):
		x, y, z = state
		return [
			-y - z,
			x + a * y,
			b + z * (x - c)
		]
	
	a = 0.2
	b = 0.2
	c_values = [2.5, 3.5, 4.0, 5.7]
	
	t_span = (0, 500)
	t_eval = np.linspace(0, 500, 120000)
	
	
	for c in c_values:
	
		sol = solve_ivp(
			rossler,
			t_span,
			[1.0, 1.0, 1.0],
			args=(a, b, c),
			t_eval=t_eval,
			method="RK45"
		)
	
		x, y, z = sol.y
	
		cut = int(0.2 * len(x))
		x = x[cut:]
		y = y[cut:]
	
		plt.figure(figsize=(6, 6))
		plt.plot(x, y, linewidth=0.5, color="black")
	
		plt.xlabel("x")
		plt.ylabel("y")
		plt.axis("equal")
		plt.grid(True)
	
	
		plt.show()