	import numpy as np
	from scipy.integrate import solve_ivp
	from numpy.linalg import qr
		
	a, b, c = 0.2, 0.2, 5.7
		
	def rossler(t, state):
		x, y, z = state
		return np.array([
			-y - z,
			x + a * y,
			b + z * (x - c) 
		])
		
	def jacobian(state):
		x, y, z = state
		
		return np.array([
			[0, -1, -1],
			[1, a, 0],
			[z, 0, x - c]  
	    ])
		
	def augmented(t, Y):
		state = Y[:3]
		Q = Y[3:].reshape(3, 3)
		
		dstate = rossler(t, state)
		J = jacobian(state)
		dQ = J @ Q
		
		return np.concatenate([dstate, dQ.flatten()])
		
	dt = 0.02
	T_total = 5000         
	n_steps = int(T_total / dt)
		
	orthonorm_step = 10     
		
	state0 = np.array([1.0, 1.0, 1.0])
	Q = np.eye(3).flatten()
	Y = np.concatenate([state0, Q])
		
	lyap_sum = np.zeros(3)
		
	t = 0.0
		
	for i in range(n_steps):
		
		sol = solve_ivp(
			augmented,
			(t, t + dt),
			Y,
			method="RK45",
			rtol=1e-9,
			atol=1e-12  )
		
		Y = sol.y[:, -1]
		t += dt
		
		state = Y[:3]
		Qmat = Y[3:].reshape(3, 3)
		
		if i % orthonorm_step == 0:
			Qmat, R = qr(Qmat)
	
			lyap_sum += np.log(np.abs(np.diag(R)))
		
			Q = Qmat.flatten()
			Y[3:] = Q
		
	lyapunov = lyap_sum / (T_total)