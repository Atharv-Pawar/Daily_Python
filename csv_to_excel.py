import pandas as pd

# csv_to_excel.py
def csv_to_excel(csv_file, excel_file):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Write to an Excel file
        df.to_excel(excel_file, index=False)
        print(f"Converted {csv_file} to {excel_file}")
    except Exception as e:
        print(f"Error converting {csv_file} to {excel_file}: {e}")

def excel_to_csv(excel_file, csv_file):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        
        # Write to a CSV file
        df.to_csv(csv_file, index=False)
        print(f"Converted {excel_file} to {csv_file}")
    except Exception as e:
        print(f"Error converting {excel_file} to {csv_file}: {e}") 