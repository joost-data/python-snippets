from openpyxl import Workbook

def write_excel(filename, headers, rows):
    """
    Write tabular data to an Excel file.
    """
    wb = Workbook()
    ws = wb.active
    ws.append(headers)
    for row in rows:
        ws.append(row)
    wb.save(filename)

