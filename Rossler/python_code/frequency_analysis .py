	import numpy as np
	import matplotlib.pyplot as plt
	from scipy.integrate import solve_ivp
		
	a, b = 0.2, 0.2
		
	c_values = [2.5, 3.5, 4,
	
	 5.7]
		
	def rossler(t, state, c):
		x, y, z = state
		return [
			-y - z,
			x + a*y,
			b + z*(x - c)
		]
		
	t_eval = np.linspace(0, 1000, 200000)
		
	for c in c_values:
		
		sol = solve_ivp(
			rossler,
			(0, 1000),
			[1, 1, 1],
			args=(c,),
			t_eval=t_eval,
			method='RK45'
		)
		
		x = sol.y[0]
		
		x = x[50000:]
		
		dt = t_eval[1] - t_eval[0]
		
		N = len(x)
		freq = np.fft.rfftfreq(N, d=dt)
		power = np.abs(np.fft.rfft(x - np.mean(x)))**2
		
	
	plt.figure(figsize=(7,4))
		
	plt.semilogy(
		freq,
		power,
		color='black',
		lw=0.6
	)
		
	plt.xlim(0, 0.5)
		
	plt.xlabel("Frequency")
	plt.ylabel("Power")
		
		
	plt.grid(True)
		
	plt.show()
		
				