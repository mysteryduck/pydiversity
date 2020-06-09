import pandas as pd
import numpy as np

data = pd.read_csv('partition.csv')

#type(data)
#data.columns
#pd.melt(data, id_vars = 'species')


a = metacommunity(data)
a.species
a.type_abundance

a.raw_alpha()
a.norm_alpha()
