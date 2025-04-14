import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

results = pd.read_csv("figures_170000p\simulation_results.csv", delimiter = ";")


results["Coverage"] = (170000-results["P"]) / 170000


####
##### S-curve
####
plt.figure(figsize=(3, 6))
plt.plot(results["R"], results["Coverage"], marker='o', linestyle='-', label="k_ratio = 10^6")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("R")
plt.ylabel("Coverage")
plt.ylim(5.5e-7,1.1)
plt.title("Coverage vs Free Receptors")
plt.legend()
plt.savefig(f"figures_170000p/Simulation_S_Curve.pdf", dpi=300, bbox_inches="tight") #store the plot in the figures folder
plt.show()
plt.clf()   # clear the plotting for the next figure


####
##### Alpha plot
####

derivative = np.gradient(np.log(results['Coverage']), np.log(results['R']))
mean = np.mean(derivative)

plt.figure(figsize=(3, 6))
plt.plot(results["R"], derivative, color='Blue', zorder=2.5, marker='o', linestyle='-')
max_alpha_index = np.argmax(derivative)
max_alpha_R = results["R"][max_alpha_index]
print(f'Max Alpha (R={max_alpha_R:.2e})')
#plt.axvline(x=max_alpha_R, color='black', linestyle='--', linewidth = 0.5,label=f'Max Alpha (R={max_alpha_R:.2e})')
#plt.legend()
plt.axhline(y=1, xmin=0, xmax=1, linewidth=1, color='slategrey')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("R")
plt.ylabel("Alpha")
plt.ylim(0,25)
plt.title("Alpha vs Free Receptors")
plt.savefig(f"figures_170000p/Simulation_Alpha_Plot.pdf", dpi=300, bbox_inches="tight") #store the plot in the figures folder
plt.show()
plt.clf()   # clear the plotting for the next figure
