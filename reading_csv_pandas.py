import pandas as pd 

# to start the localhost, place the required file in any folder an do the following command
# $ python -m http.server 8080
ministries_df = pd.read_csv("http://localhost:8080/pak-fed-ministries.csv", index_col='Name of Ministry')

print(ministries_df)