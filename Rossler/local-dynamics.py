	import numpy as np
  	from scipy.integrate import solve_ivp
  	import matplotlib.pyplot as plt
  	
  	a, b, c = 0.2, 0.2, 5.7
  	
  	
  	def equilibrium(sign=1):
  		z = (c + sign * np.sqrt(c**2 - 4 * a * b)) / (2 * a)
  		x = a * z
  		y = -z
  		return np.array([x, y, z])
  		
  	
  	def jacobian(E):
  		return np.array([
  			[0, -1, -1],
  			[1, a, 0],
  			[E[2], 0, E[0] - c]
  		])
  	
  	
  	def linear_dynamics(E, t_span=(0, 20), n=4000):
  	
  		J = jacobian(E)
  	
  		def lin_system(t, x):
  			return J @ x
  	
  		x0 = np.array([1e-4, 0.0, 1e-4])
  		t_eval = np.linspace(*t_span, n)
  	
  		sol = solve_ivp(lin_system, t_span, x0, t_eval=t_eval)
  	
  		return sol.y.T + E
  	
  	
  	def plot_orbit(X, E):
  	
  		fig = plt.figure(figsize=(8, 6))
  		ax = fig.add_subplot(111, projection='3d')
  	
  		ax.plot(X[:, 0], X[:, 1], X[:, 2],
  			color='black', linewidth=1.2)
  		ax.scatter(E[0], E[1], E[2],
  			color='black', s=80)
  	
  		ax.set_xlabel("$x$")
  		ax.set_ylabel("$y$")
  		ax.set_zlabel("$z$")
  	
  		ax.ticklabel_format(useOffset=False, style='plain')
  	
  		ax.xaxis.get_major_formatter().set_useOffset(False)
  		ax.yaxis.get_major_formatter().set_useOffset(False)
  		ax.zaxis.get_major_formatter().set_useOffset(False)
  	
  		ax.view_init(elev=25, azim=45)
  		ax.grid(True)
  	
  		plt.tight_layout()
  		
  		plt.show()
  	
  	
  	# E1
  	E1 = equilibrium(sign=+1)
  	X1 = linear_dynamics(E1)
  	plot_orbit(X1, E1)
  	
  	# E2
  	E2 = equilibrium(sign=-1)
  	X2 = linear_dynamics(E2)
  	plot_orbit(X2, E2)