import tellurium as te
import roadrunner
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the reaction network using Antimony string
"""
The species of the gillespie algorithm are defined as P(number of arms
bound).
This means that P1 is a particle with one bound arm, P2 a particle with
2 bound arms etc.
"""
model = te.loada('''
// Species
species P, R, P1, P2, P3, P4, P5, P6;
// Parameters
k_on_sol = 0.00000001;
k_off = 1;
k_on_surf = 100000000000000;
// Reactions
P + R -> P1; k_on_sol * P * R;
P1 -> P + R; k_off * P1;
P1 + R -> P2; k_on_surf * P1 * R;
P2 -> P1 + R; k_off * P2
P2 + R -> P3; k_on_surf * P2 * R;
P3 -> P2 + R; k_off * P3
P3 + R -> P4; k_on_surf * P3 * R;
P4 -> P3 + R; k_off * P4
P4 + R -> P5; k_on_surf * P4 * R;
P5 -> P4 + R; k_off * P5
P5 + R -> P6; k_on_surf * P5 * R;
P6 -> P5 + R; k_off * P6
// Initial conditions
P = 17000;
R = 100;
P1 = 0;
P2 = 0;
P3 = 0;
P4 = 0;
P5 = 0;
P6 = 0;
''')


###
#### Parameters
###

ending_n = 400

###
#### Get parameters
###

Species = model.getFloatingSpeciesIds() #get list with species = ["P", "R", ...]
initial_conditions = {species: model[species] for species in Species} # Get initial conditions of the model = values of the species

Results = pd.DataFrame(columns=["P", "R", "P1", "P2", "P3", "P4", "P5", "P6"]) #Create empty df with column shits

# Create the "figures" directory if it doesn't exist
os.makedirs("figures", exist_ok=True)

###
#### Define Simulation Function
###

def run_sim(model, NR, db):

    
    model.R = NR # set the number of receptors to NR
    model.P = 17000
    model.P1 = 0
    model.P2 = 0
    model.P3 = 0
    model.P4 = 0
    model.P5 = 0
    model.P6 = 0


    # Run a stochastic simulation using Gillespie's algorithm
    result = model.gillespie(0, 1000, 500) # run sim (start_time, end_time, steps)

    # Calculate the average of the last ending_n values for each species
    averages = {species: np.round(np.mean(result[-ending_n:, i+1]), 2) for i, species in enumerate(Species)}
    #print(f"Averages of the last {ending_n} values for each species: {averages}")

    #Store the values in the database (db)
    db.loc[len(db)] = averages

    # Plot results
    for i in range(len(Species)):
        plt.plot(result[:, 0], result[:, i+1], label=Species[i])


###
#### Run simulation for all NRs wanted
###

receptor_array = np.round(np.logspace(np.log10(100), np.log10(100000), num=10)) #make array with all number of receptors we need to check

for num,i in enumerate(receptor_array):
    run_sim(model, i, Results)  #run simulation with NR
    #final_conditions = {species: model[species] for species in Species} # Get final conditions of the model = values of the species
    print(num)

    plt.title(f'Gillespie Simulation\nNR = {i}', size=10)
    plt.xlabel('Time')
    plt.ylabel('Molecule Count')
    plt.legend()
    plt.savefig(f"figures/Simulation_NR_{i}.pdf", dpi=300, bbox_inches="tight") #store the plot in the figures folder
    #plt.show()
    plt.clf()   # clear the plotting for the next figure


Results.to_csv("figures/simulation_results.csv", sep = ";", index=False)    #save results as a csv file
print(Results)  #print the table 


