import os
import pandas as pd

# Set directory path and file name
directory_path = 'C:/Users/Hopi/Awork/da-assignment'
file_name = 'data.xlsx'
file_path = os.path.join(directory_path, file_name)

df = pd.read_excel(file_path, sheet_name='Sheet1')

## Print data 1
# print(df.head())

# Data cleaning
columns_of_interest = [
    'Country', '3_Gender', '4_Age', '5_Generation', '234_Happy', 
    '235_Relaxed_and_content', '236_Connected_to_others', 
    '230_Secure', '238_Productive', '239_Hopeful_for_the_future'
]
filtered_data = df[columns_of_interest]

filtered_data.columns = [
    'Country', 'Gender', 'Age', 'Generation', 'Happy', 
    'Relaxed_and_Content', 'Connected_to_Others', 
    'Secure', 'Productive', 'Hopeful_for_the_Future'
]

## Print data 2
# print(filtered_data.head())

# Drop rows with missing values & turn "Yes/No" to "1/0"
filtered_data.replace({'Yes': 1, 'No': 0}, inplace=True)
filtered_data.dropna(inplace=True)

## Print data 3
# print(filtered_data.head())

# Save data to "cleaned_data.xlsx"
output_file_name = 'cleaned_data.xlsx'
output_file_path = os.path.join(directory_path, output_file_name)

filtered_data.to_excel(output_file_path, index=False)

print(f"Filtered data saved to: {output_file_path}")

# Filter out Netherlannds (only Swden and Spain)
sweden_data = filtered_data[filtered_data['Country'] == 'Sweden']
spain_data = filtered_data[filtered_data['Country'] == 'Spain']

# print data 4
print("Sweden Data")
print(sweden_data.head())
print("Spain Data")
print(spain_data.head())

# Test Correlation between variables
# sweden_corr = sweden_data.corr()
# spain_corr = spain_data.corr()
sweden_corr = sweden_data.select_dtypes(include=[float, int]).corr()
spain_corr = spain_data.select_dtypes(include=[float, int]).corr()

# Print 4 : correlation matrix
print("Correlation Matrix :")
print("Sweden Correlation Matrix")
print(sweden_corr)
print("Spain Correlation Matrix")
print(spain_corr)