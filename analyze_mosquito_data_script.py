import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

data = pd.read_csv(filename, index_col = 'year')

data['temperature'] = mosquito_lib.fahr_to_celsius(data['temperature'])
print data.head()

parameters = mosquito_lib.analyze(data)
print parameters
