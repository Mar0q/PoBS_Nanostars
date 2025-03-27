import numpy as np

# Create an array from 100 to 100000 sampled on a log scale
log_scale_array = np.logspace(np.log10(100), np.log10(100000), num=100   )
import matplotlib.pyplot as plt

# Generate random values between -10 and 10 for each time step
random_values = np.random.uniform(5, 10, size=log_scale_array.shape)

# Plot the data on a logx scale
plt.figure()
plt.plot(log_scale_array, random_values, marker='o', linestyle='-', label='Random Values')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Log-Scaled Time Steps')
plt.ylabel('Random Values')
plt.title('Random Values vs Log-Scaled Time Steps')
plt.legend()
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.show()