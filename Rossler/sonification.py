import numpy as np
	from scipy.integrate import solve_ivp
	from scipy.io import wavfile
	from IPython.display import Audio, display
	
	def rossler_system(t, state, a, b, c):
		x, y, z = state
		dxdt = -y - z
		dydt = x + a * y
		dzdt = b + z * (x - c)
		return [dxdt, dydt, dzdt]
	
	def generate_rossler_sound(c_value, filename,
	 	duration = 5.0, sample_rate = 44100):
		a = 0.2
		b = 0.2
		time_scale = 1375.0
		t_max = duration * time_scale
	
		t_eval = np.linspace(0, t_max, int(sample_rate * duration))
	
		initial_state = [0.1, 0.0, 0.1]
	
		sol = solve_ivp(
			rossler_system,
			(0, t_max),
			initial_state,
			args=(a, b, c_value),
			t_eval=t_eval,
			method='RK45'
		)
	
		x_signal = sol.y[0]
	
		transient_cutoff = int(len(x_signal) * 0.1)
		x_signal = x_signal[transient_cutoff:]
	
		x_signal = x_signal - np.mean(x_signal)
	
		max_val = np.max(np.abs(x_signal))
		if max_val > 0:
			x_signal = x_signal / max_val
	
		audio_data = (0.9 * x_signal * 32767).astype(np.int16)
		 
		wavfile.write(filename, sample_rate, audio_data)
	
		print(f"File {filename} successfully generated.")
		display(Audio(filename))
	
	
	generate_rossler_sound(c_value=2.5, filename="rossler_periodic_25.wav")
	generate_rossler_sound(c_value=5.7, filename="rossler_chaotic_57.wav")