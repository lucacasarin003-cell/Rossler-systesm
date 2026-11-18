	import numpy as np
		
	a, b, c = 0.2, 0.2, 5.7
		
	for sign in [+1, -1]:
		
		z = (c + sign * np.sqrt(c**2 - 4*a*b)) / (2*a)
		x = a * z
		y = -z
		
		E = np.array([x, y, z])
		
		J = np.array([
		[0, -1, -1],
		[1, a, 0],
		[z, 0, x - c]  
		])
		
		eigvals, eigvecs = np.linalg.eig(J)
			
		print("Equilibrium E =", E)
		print("Eigenvalues =", eigvals)
		print("Eigenvectors =", eigvecs)