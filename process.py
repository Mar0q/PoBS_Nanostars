import pandas as pd
import matplotlib.pyplot as plt

results = pd.read_csv("figures\simulation_results.csv", delimiter = ";")


results["Coverage"] = (170000-results["P"]) / 170000

print(results)


plt.figure(figsize=(3, 6))
plt.plot(results["R"], results["Coverage"], marker='o', linestyle='-', label="k_ratio = 10^6")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("R")
plt.ylabel("Coverage")
plt.title("Coverage vs Free Receptors")
plt.legend()
plt.show()
