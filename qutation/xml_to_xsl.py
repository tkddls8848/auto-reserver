import os
from queue import Empty
import xml.etree.ElementTree as Et
from openpyxl import Workbook
from collections import defaultdict


xmlparse = Et.parse(os.getcwd() + '\\qutation\\tmp\\E1080.xml')
root = xmlparse
data_dict = defaultdict(list)

# CFXML => CFData => ProductLineItem =>
# key : ProductIdentification =>ProprietaryProductIdentifier =>{ProductDescription:,ProductTypeCode:,}, 
# key : UnitListPrice => FinancialAmount {GlobalCurrencyCode, MonetaryAmount} 
# key : MaintenanceUnitListPrice => FinancialAmount {GlobalCurrencyCode, MonetaryAmount} 
# key : ProductSubLineItem => {위 키 3개 반복}
def save_excel():
    w_book = Workbook()
    w_sheet = w_book.active
    w_sheet.cell(row=1, column=1).value = 'START'
    for _ in root.getroot().iter():
        product_quantity = 0
        product_id = []
        product_cost = []
        if _.tag == "ProductSubLineItem":
            print("ProductSubLineItem", i)
        if _.tag == "Quantity":
            print()
            print(_.tag, _.text)
            product_quantity = int(_.text)
            print(product_quantity)
        elif _.tag == "ProductIdentification":
            for i in _.iter():
                if i.tag == "ProprietaryProductIdentifier":
                    print("Model No.", i.text)
                    product_id.append(i.text)
                elif i.tag == "ProductDescription":
                    print("Description", i.text)
                    product_id.append(i.text)
                elif i.tag == "ProductTypeCode":
                    print("ITEM", i.text)    
                    product_id.append(i.text)                                   
        elif _.tag == "UnitListPrice":
            for i in _.find("FinancialAmount"):
                if i.tag == "MonetaryAmount":
                    print("cost", i.text)
                    product_cost.append(i.text)
        elif _.tag == "MaintenanceUnitListPrice":
            print("MaintenanceUnitListPrice", _)   
            product_cost.append(_.text)     
        if product_id != []:
            print(product_id)
        if product_cost != []:
            print(product_cost)
    
    w_book.save(os.getcwd() + '\\qutation\\tmp\\samples.xlsx')

save_excel()