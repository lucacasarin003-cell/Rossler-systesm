import numpy as np
	import matplotlib.pyplot as plt
	from scipy.integrate import solve_ivp
	from scipy.signal import find_peaks
		
	a, b, c = 0.2, 0.2, 5.7
		
	def rossler(t, state):
		x, y, z = state
		return [-y - z, x + a*y, b + z*(x - c)]
		
	t0, tf = 0, 30000
	t_eval = np.arange(t0, tf, 0.01) 
		
	sol = solve_ivp(
		rossler, 
		[t0, tf],
		[1.0, 1.0, 1.0],
		method='RK45',
		t_eval=t_eval 
	 )
		
	t_full = sol.t
	x_full = sol.y[0]
		
	transient_time = 5000
	mask = t_full > transient_time
	x = x_full[mask]
		
	peaks, _ = find_peaks(x, distance=10)
	maxima = x[peaks]
		
	x_n = maxima[:-1]
	x_n1 = maxima[1:]
		
	plt.figure(figsize=(7, 7))
	plt.plot(x_n, x_n1, '.', color='#030914', markersize=0.3, alpha=0.5)
		
	plt.xlabel(r'$x_n$', fontsize=14)
	plt.ylabel(r'$x_{n+1}$', fontsize=14)
	
	plt.tight_layout()
		
		
	plt.show()