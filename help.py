import pandas as pd

# Replace 'path/to/your/file.csv' with the actual path to your CSV file

# Read the CSV file using with open
data = []
with open('species.csv', 'r', encoding='windows-1252') as file:
    for line in file:
        data.append(line.strip().split(','))  # Split each line into a list of values

# Convert the data list into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df.head(10))