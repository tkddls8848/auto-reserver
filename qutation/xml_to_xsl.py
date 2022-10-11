import datetime
from openpyxl import Workbook


w_book = Workbook()
w_sheet = w_book.active

w_sheet['A1'] = 'asdf'
w_sheet.append([1,2,3])
w_sheet['C4'] = datetime.datetime.now()

w_book.save('sample.xlsx')
