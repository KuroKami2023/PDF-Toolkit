import sys
import tabula
import pandas as pd

def convert_pdf_to_excel(pdf_path, output_path):
    # Extract tables from PDF into a DataFrame list
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Write each DataFrame to an Excel sheet
    with pd.ExcelWriter(output_path) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f'Sheet_{i+1}', index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_excel.py <pdf_file_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    excel_path = pdf_path.replace('.pdf', '.xlsx')

    convert_pdf_to_excel(pdf_path, excel_path)
