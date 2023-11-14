from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "나도Sheet"
wb.save("sample.xlsx")
wb.close()
