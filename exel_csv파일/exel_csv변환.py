import pandas as pd
import os

# 엑셀 파일 경로 설정 (경로 앞에 r을 붙여 raw string으로 사용)
excel_file_path = r'C:/Users/samsung/OneDrive/DT교육/HE0IN_Process_status_project/project_excel_fie/5.xlsx'

# 출력 폴더 경로 설정
output_folder = r'C:/Users/samsung/OneDrive/DT교육/HE0IN_Process_status_project/output5/'

# 출력 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 엑셀 파일 불러오기
excel_data = pd.ExcelFile(excel_file_path)

# 각 시트를 불러와서 CSV로 저장
for sheet_name in excel_data.sheet_names:
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    csv_file_path = os.path.join(output_folder, f"{sheet_name}.csv")  # CSV 파일 경로 설정
    df.to_csv(csv_file_path, index=False)
    print(f"{sheet_name} 시트를 {csv_file_path} 파일로 저장했습니다.")
