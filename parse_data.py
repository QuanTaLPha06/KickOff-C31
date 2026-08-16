import openpyxl
import json
import os
import glob

def parse_excel():
    wb = openpyxl.load_workbook('Untitled spreadsheet.xlsx')
    sheet = wb.active
    
    headers = []
    rows = []
    
    for i, row in enumerate(sheet.iter_rows(values_only=True)):
        if i == 0:
            headers = [str(c).strip() if c is not None else f'col_{j}' for j, c in enumerate(row)]
            continue
        if not any(row):
            continue
        
        row_dict = {}
        for j, val in enumerate(row):
            if j < len(headers):
                row_dict[headers[j]] = str(val).strip() if val is not None else ''
        rows.append(row_dict)
        
    print(f"Total headers: {headers}")
    print(f"Total players in Excel: {len(rows)}")
    with open('parsed_players.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
    
    # Print sample
    for r in rows[:5]:
        print(r)

if __name__ == '__main__':
    parse_excel()
