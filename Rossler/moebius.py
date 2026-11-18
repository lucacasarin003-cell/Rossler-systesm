	import numpy as np
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D
		
	
	theta = np.linspace(0, 2 * np.pi, 150)
	w = np.linspace(-2.5, 2.5, 32)  
	Theta, W = np.meshgrid(theta, w)
		
	
	R = 6.5 
	X = (R + W * np.cos(Theta / 2)) * np.cos(Theta)
	Y = (R + W * np.cos(Theta / 2)) * np.sin(Theta)
	Z = W * np.sin(Theta / 2)
		
	
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111, projection='3d')
		
		
	surf = ax.plot_surface(
			X, Y, Z,
			cmap='bone',
			edgecolor='black',
			linewidth=0.3,
			alpha=0.8,
			shade=True
	)
		
	
	ax.set_xlabel("x", fontsize=11)
	ax.set_ylabel("y", fontsize=11)
	ax.set_zlabel("z", fontsize=11)
		
	
	ax.set_xlim(-10, 10)
	ax.set_ylim(-10, 10)
	ax.set_zlim(-5, 5) 
		
	
	
	ax.view_init(elev=22, azim=-55)
		

	plt.tight_layout()
		
		
	plt.show()