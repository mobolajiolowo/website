import pandas as pd

# Read JSON data into a DataFrame
species_df = pd.read_csv('species.csv')

# Display the DataFrame
search_input = input("Enter")
species_row= species_df[species_df['species'].str.contains(search_input, case=False) |
                          species_df['keys'].str.contains(search_input, case=False)]
    
#species_name = species_row['species'].values
#keys = species_row['keys'].values
print(species_row)
#print(keys)
