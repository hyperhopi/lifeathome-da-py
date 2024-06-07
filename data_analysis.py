import os
import pandas as pd
directory_path = 'C:/Users/Hopi/Awork/da-assignment'
file_name = 'data.xlsx'
file_path = os.path.join(directory_path, file_name)

df = pd.read_excel(file_path, sheet_name='Sheet1')

df['2_INGKA/Non-INGKA'] = df['2_INGKA/Non-INGKA'].replace('INGKA', 'INGKAS')

output_file_name = 'cleaned_data.xlsx'
output_file_path = os.path.join(directory_path, output_file_name)

df.to_excel(output_file_path, index=False)
print(df.head())