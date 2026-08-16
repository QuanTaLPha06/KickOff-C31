import zipfile
import xml.etree.ElementTree as ET
import json

def parse_xlsx(filename):
    with zipfile.ZipFile(filename, 'r') as z:
        # Load shared strings
        shared_strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            ss_tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            # namespace
            ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            for si in ss_tree.findall('.//main:si', ns):
                t = si.find('.//main:t', ns)
                if t is not None and t.text:
                    shared_strings.append(t.text)
                else:
                    # check all text inside si
                    text = "".join(si.itertext())
                    shared_strings.append(text)
        
        # Load sheet1
        sheet_tree = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        
        rows = []
        for row_elem in sheet_tree.findall('.//main:row', ns):
            row_data = []
            for c_elem in row_elem.findall('.//main:c', ns):
                cell_type = c_elem.get('t')
                v_elem = c_elem.find('main:v', ns)
                val = v_elem.text if v_elem is not None else ""
                
                if cell_type == 's' and val != "":
                    idx = int(val)
                    if idx < len(shared_strings):
                        val = shared_strings[idx]
                row_data.append(val)
            rows.append(row_data)
            
        return rows

if __name__ == '__main__':
    rows = parse_xlsx('Untitled spreadsheet.xlsx')
    with open('parsed_excel_rows.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
    print(f"Total rows extracted: {len(rows)}")
    for r in rows[:15]:
        print(r)
