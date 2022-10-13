from openpyxl import load_workbook, Workbook

c_name = 1
c_id = 2
c_money = 3

default_money = 30000000

wb = load_workbook("./db/userDB.xlsx")
ws = wb.active

def signup(_name, _id):
    ws.cell(row=2, column=c_name, value = _name)
    ws.cell(row=2, column=c_id, value = _id)
    ws.cell(row=2, column=c_money, value = default_money)

    wb.save('./db/userDB.xlsx')