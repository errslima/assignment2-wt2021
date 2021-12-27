import pandas as pd
import numpy as np
import re
# import ipynb.fs.defs.functions2 as enzo

# Remove restrictions on amount of rows and columns that can be displayed in pandas dataframes.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data = pd.read_csv("data/US_Accidents_June20.csv")