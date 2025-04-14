import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

results = pd.read_csv("figures_170000p\simulation_results.csv", delimiter = ";")


results["Coverage"] = (170000-results["P"]) / 170000

print(results)


####
##### S-curve
####
plt.figure(figsize=(3, 6))
plt.plot(results["R"], results["Coverage"], marker='o', linestyle='-', label="k_ratio = 10^6")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("R")
plt.ylabel("Coverage")
plt.title("Coverage vs Free Receptors")
plt.legend()
plt.savefig(f"figures/Simulation_S_Curve.pdf", dpi=300, bbox_inches="tight") #store the plot in the figures folder
plt.show()
plt.clf()   # clear the plotting for the next figure


####
##### Alpha plot
####

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
plt.savefig(f"figures/Simulation_Alpha_Plot.pdf", dpi=300, bbox_inches="tight") #store the plot in the figures folder
plt.show()
plt.clf()   # clear the plotting for the next figure
