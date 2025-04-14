import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

results = pd.read_csv("figures_170000p\simulation_results.csv", delimiter = ";")
results["Coverage"] = (170000-results["P"]) / 170000

derivative = np.gradient(np.log(results['Coverage']), np.log(results['R']))
mean = np.mean(derivative)

plt.figure(figsize=(3, 6))
plt.plot(results["R"], derivative, color='Blue', zorder=2.5)
plt.axhline(y=mean, xmin=0, xmax=1, linewidth=1, color='slategrey')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("R")
plt.ylabel("Alpha")
plt.title("Alpha vs Free Receptors")
plt.show()