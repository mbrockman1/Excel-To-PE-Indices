import pandas as pd
from pe_funcs.pe_indices_funcs import *

INPUT_FILE = '' #place input xlsx file
df = pd.read_excel(INPUT_FILE)


df.columns = ['MRN', 'Age', 'Sex', 'Cancer', 'CHF_COPD', 'HR', 'SBP', 'RR', 'Temp', 'SpO2', 'TnI', 'RV function']
df.index_col = 'MRN'


pesi_list = [pesi_score(y) for x, y in df.iterrows()]    
spesi_list = [simple_pesi_score(y) for x, y in df.iterrows()]
esc_list = [esc_score(y) for x, y in df.iterrows()]
bova_list = [bova_score(y) for x, y in df.iterrows()]


df['PESI'] = pesi_list
df['simple PESI'] = spesi_list
df['ESC 2019'] = esc_list
df['BOVA'] = bova_list
df.to_excel('./updated_data.xlsx')