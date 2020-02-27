import pandas as pd 
from pak_fed_ministries_data import get_ministries_data

ministries = get_ministries_data()

ministries_df = pd.DataFrame(ministries).set_index('text')
ministries_df.reset_index().to_json("./pak-fed-ministries_2.json", orient='records')