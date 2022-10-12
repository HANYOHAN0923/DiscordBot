from openpyxl import load_workbook, Workbook

c_name = 1
c_id = 2
c_money = 3
c_lvl = 4

default_money = 30000000

wb = load_workbook(filename='/Users/han-yohan/Development/PYTHON_LABS/Discord/lib/userDB.xlsx')
ws = wb.active


def signup(_name, _id):
    _row = checkRow()

    ws.cell(row=_row, column=c_name, value=_name)
    ws.cell(row=_row, column=c_id, value=_id)
    ws.cell(row=_row, column=c_money, value=default_money)
    ws.cell(row=_row, column=c_lvl, value=1)

    wb.save("")

def checkRow():
    for row in range(2, ws.max_row + 1):
        if ws.cell(row,1).value is None:
            return row

def checkName(_name, _id):
    for row in range(2, ws.max_row+1):
        if ws.cell(row,1).value == _name and ws.cell(row,2).value == _id:
            return False
        else:
            return True