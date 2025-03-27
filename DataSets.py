import pandas as pd

def get_data (data_path):
    #Get data from the file
    OG_df = pd.read_csv(data_path, delimiter = ";")

    # Separate the columns into two dataframes, SP= Simulation Parameters and Data= Data
    SP_df= OG_df[['Simulation parameters', 'Unnamed: 2']]   # Get the simulation data
    Data_df = OG_df.drop(columns=['Simulation parameters', 'Unnamed: 1', 'Unnamed: 2'])

    ### Deal with the Simulation Parameters Dataframe
    SP_df = SP_df.dropna() # Drop rows with NaN values in SP_Main_df
    SP_df = SP_df.rename(columns={'Unnamed: 2': 'Values'}) #Change the column name

    ### Deal with the Data Dataframe
    Data_df = Data_df.loc[:, ~Data_df.columns.str.contains('^Unnamed:')]
    Data_df = Data_df.dropna() # Drop rows with NaN values in Data_Main_df

    return SP_df, Data_df

SP_Main_df, Data_Main_df = get_data('DataSet_Nanostars_MAIN.csv')
SP_Set1_df, Data_Set1_df = get_data('DataSet_Nanostars_Set1.csv')
SP_Set2_df, Data_Set2_df = get_data('DataSet_Nanostars_Set2.csv')
SP_Set3_df, Data_Set3_df = get_data('DataSet_Nanostars_Set3.csv')
SP_Set4_df, Data_Set4_df = get_data('DataSet_Nanostars_Set4.csv')
SP_Set5_df, Data_Set5_df = get_data('DataSet_Nanostars_Set5.csv')
SP_Set6_df, Data_Set6_df = get_data('DataSet_Nanostars_Set6.csv')
SP_Set7_df, Data_Set7_df = get_data('DataSet_Nanostars_Set7.csv')

SP_list = [SP_Main_df, SP_Set1_df, SP_Set2_df, SP_Set3_df, SP_Set4_df, SP_Set5_df, SP_Set6_df, SP_Set7_df]
Data_list = [Data_Main_df, Data_Set1_df, Data_Set2_df, Data_Set3_df, Data_Set4_df, Data_Set5_df, Data_Set6_df, Data_Set7_df]

# Add a column to the dataframes to identify the set
for i in range(len(SP_list)):
    SP_list[i]["Set"] = i   
    Data_list[i]["Set"] = i

# Calculate the ratios of the values in the dataframes
for i in range(len(SP_list)):
    SP_list[i]["k_ratio"] = float(SP_list[i].loc[2]["Values"])/float(SP_list[i].loc[3]["Values"])

#Get ratios
#Data_Main_df["k_ratios"] = SP_Main_df["k_"]

# Concatenate all the dataframes
SP_df = pd.concat(SP_list)
Data_df = pd.concat(Data_list)
