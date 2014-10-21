import sys
import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

#filename = "A1_mosquito_data.csv"
filename = sys.argv[1]

print "Analyzing", filename

data = pd.read_csv(filename, index_col = 'year')

# Change temperature to Celsius
data['temperature'] = mosquito_lib.fahr_to_celsius(data['temperature'])
print data.head()

# Get parameters from analyze()
parameters = mosquito_lib.analyze(data, filename.replace("csv", "png"))
print parameters

# Write parameters to .csv
parameters.to_csv(filename.replace("data", "parameters"))
