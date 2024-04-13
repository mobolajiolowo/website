from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)



# Load species data from JSON file
species_df = pd.read_csv('species.csv',encoding='windows-1252')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/how_to_use')
def how_to_use():
    return render_template('how_to_use.html')

@app.route('/search', methods=['POST'])
def search_species():
    search_input = request.form['search_input']
    
    # Search by species name or keys
    species_row = species_df[species_df['species'].str.contains(search_input, case=False) |
                             species_df['keys'].str.contains(search_input, case=False)]
    
    if not species_row.empty:
      species_name = species_row['species'].values[0]
      keys = species_row['keys'].values[0]
      description = species_row['description'].values[0]
      location = species_row['location'].values[0]
      
    else:
     species_name = None
     keys = None

    return render_template('search_results.html',       species_name=species_name, keys=keys, location=location, description = description, search_input=search_input)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
