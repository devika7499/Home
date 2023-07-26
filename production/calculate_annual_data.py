import pandas as pd

data = pd.read_excel("production_data.xls")

# Calculate annual production for each well based on API WELL NUMBER
annual_data = data.groupby("API WELL  NUMBER").sum().reset_index()
