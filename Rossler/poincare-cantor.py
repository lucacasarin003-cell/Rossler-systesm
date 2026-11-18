	import numpy as np
	import matplotlib.pyplot as plt
	from scipy.integrate import solve_ivp
	
	a, b, c = 0.2, 0.2, 5.7
	
	def rossler(t, state):
		x, y, z = state
		return [
			-y - z,
			x + a*y,
			b + z*(x-c)
		]
	
	# Poincare section

	def x_crossing(t, state):
		return state[0]
	
	x_crossing.direction = 1
	x_crossing.terminal = False
	
	sol = solve_ivp(
		rossler,
		(0, 5000),
		[1.0, 1.0, 1.0],
		method="RK45",
		max_step=0.02,
		events=x_crossing
	)
	
	events = sol.y_events[0]
	
	events = events[500:]
	
	poincare_y = events[:,1]
	poincare_z = events[:,2]
	
	
	plt.figure(figsize=(6,6))
	
	plt.scatter(
		poincare_y,
		poincare_z,
		s=0.3,
		color="black"
	)
	
	plt.xlabel(r"$y$")
	plt.ylabel(r"$z$")
	plt.grid(True)
	plt.tight_layout()
	
	
	plt.show()
	
	# Zoom 
	
	xmin = np.percentile(poincare_y, 45)
	xmax = np.percentile(poincare_y, 55)
	
	ymin = np.percentile(poincare_z, 45)
	ymax = np.percentile(poincare_z, 55)
	
	plt.figure(figsize=(6,6))
	
	plt.scatter(
		poincare_y,
		poincare_z,
		s=0.5,
		color="black"
	)
	
	plt.xlim(xmin, xmax)
	plt.ylim(ymin, ymax)
	
	plt.xlabel(r"$y$")
	plt.ylabel(r"$z$")
	plt.grid(True)
	plt.tight_layout()
	
	
	plt.show()
	
	# Cantor-like structure
	
	y_sorted = np.sort(poincare_y)
	
	plt.figure(figsize=(9,2))
	
	plt.plot(
		y_sorted,
		np.zeros_like(y_sorted),
		'|',
		color='black',
		markersize=8
	)
	
	plt.yticks([])
	plt.xlabel(r"$y$")
	plt.tight_layout()
	
	
	plt.show() 