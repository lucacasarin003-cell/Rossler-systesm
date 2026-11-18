import numpy as np
	import matplotlib.pyplot as plt
	from scipy.integrate import solve_ivp
		
	a, b,c  = 0.2, 0.2, 5.7
		
	def rossler(t, state):
		x, y, z = state
		
		dxdt = -y - z
		dydt = x + a*y
		dzdt = b + z*(x - c)
		
		return [dxdt, dydt, dzdt]
		
	initial_state = [1, 1, 1]
		
	t_start = 0
	t_end = 300
		
	t_eval = np.linspace(t_start, t_end, 50000)
		
	solution = solve_ivp(
		rossler,[t_start, t_end],
		initial_state,
		t_eval=t_eval,
		method='RK45'
	)
		
	x = solution.y[0]
	y = solution.y[1]
	z = solution.y[2]
		
	transient = 5000
		
	x = x[transient:]
	y = y[transient:]
	z = z[transient:]
		
	# 3D Attractor
		
	fig = plt.figure(figsize=(10, 8))
		
	ax = fig.add_subplot(111, projection='3d')
		
	ax.plot(x, y, z, color='black', lw=0.5)
		
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
		
	plt.show()
		
	# Projection x-y
		
	plt.figure(figsize=(7,7))
		
	plt.plot(x, y, color='black', lw=0.3)
		
	plt.xlabel("x")
	plt.ylabel("y")
		
	plt.axis('equal')
	plt.show()
		
	# Projection  x-z
		
	plt.figure(figsize=(7,7))
		
	plt.plot(x, z, color='black', lw=0.3)
		
	plt.xlabel("x")
	plt.ylabel("z")
		
	plt.axis('equal')
	plt.show()
		
	# Projection  y-z
		
	plt.figure(figsize=(7,7))
		
	plt.plot(y, z,color='black', lw=0.3)
		
	plt.xlabel("y")
	plt.ylabel("z")
		
	plt.axis('equal')
	plt.show()