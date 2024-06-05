import pandas as pd

file_path = file_path = 'C:\\Users\\Hopi\\OneDrive\\local and cloud\\DA\\module\\data\\data.xlsx'

df = pd.read_excel(file_path, sheet_name='Sheet1')


print(df.head())
