import datetime
import os
import xml.etree.ElementTree as Et
from openpyxl import Workbook
from collections import defaultdict

xmlparse = Et.parse(os.getcwd() + '\\qutation\\tmp\\E1080.xml')
root = xmlparse
data_dict = defaultdict(list)
ProprietaryInformation = defaultdict(object)
ProductLineItem = defaultdict(object)

def save_excel():
    w_book = Workbook()
    w_sheet = w_book.active
    w_sheet.cell(row=1, column=1).value = 'START'
    key_dict = defaultdict(list)
    
    for i in range(len(root.getroot().find('CFData').findall('ProductLineItem'))):
        print('DETAIL INFO')
        w_sheet.append(['DETAIL INFO'])
        for _ in root.getroot().find('CFData').findall('ProductLineItem')[i].find('ProductIdentification').find('PartnerProductIdentification'):
            print('KEY : ', _.tag, 'VALUE : ', _.text)
            key_dict[_.tag].append(_.text)
            w_sheet.append([_.tag, _.text])
        w_sheet.append([root.getroot().find('CFData').findall('ProductLineItem')[i].find('ProductIdentification').find('PartnerProductIdentification').text])
    print(key_dict)
    w_book.create_sheet(index=1, title='test')
    w_sheet = w_book['test']
    w_sheet.cell(row=1, column=1).value = 'NEW START'
    w_book.save(os.getcwd() + '\\qutation\\tmp\\samples.xlsx')

save_excel()