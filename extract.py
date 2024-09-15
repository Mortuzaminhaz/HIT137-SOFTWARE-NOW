import pandas as pd
import os

# Assuming the zipped folder is extracted
folder_path = r'D:\Australia\CDU\Semester_2\HIT137_SOFTWARE_NOW\Assessment_2\Answer\CSVFiles'
combined_text = ''

for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        combined_text += ' '.join(df['text'].dropna()) + '\n'

with open('combined_text.txt', 'w') as file:
    file.write(combined_text)