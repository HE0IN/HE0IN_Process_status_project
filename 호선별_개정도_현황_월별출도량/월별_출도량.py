import pandas as pd
import matplotlib.pyplot as plt

# CSV file path
csv_file_path = r'C:\Users\samsung\OneDrive\DT교육\HE0IN_Process_status_projec\HE0IN_Process_status_project\exel_csv파일\project_csv_file\호선별_개정도_현황_List(3개호선)\P1_개정도.csv'

# Load CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert '출도일자' column to datetime format
df['출도일자'] = pd.to_datetime(df['출도일자'], errors='coerce')

# Group data by month from '출도일자'
df['출도_월'] = df['출도일자'].dt.to_period('M')

# Calculate the number of entries per month
monthly_counts = df['출도_월'].value_counts().sort_index()

# Visualize monthly dispatch count
plt.figure(figsize=(10, 6))
monthly_counts.plot(kind='bar')
plt.title('Monthly Dispatch Count')
plt.xlabel('Month')
plt.ylabel('Dispatch Count')
plt.xticks(rotation=45)
plt.show()
