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

    MAIN_product_data, MAIN_product_cost = [], []
    SUB_products_data, SUB_products_cost = [], []
    for main in root.getroot().find("CFData").findall("ProductLineItem"):
        main_product_id = main.find("ProductIdentification").find("PartnerProductIdentification")
        main_product_u = main.find("UnitListPrice").find("FinancialAmount")
        sub_products = main.findall("ProductSubLineItem")


        for a in main_product_id.iter():
            if a.tag == "ProprietaryProductIdentifier":
                print("M ID", a.tag, a.text)
                MAIN_product_data.append(a.text)
        for a in main_product_u.find("MonetaryAmount").iter():
            if a.tag == "MonetaryAmount":
                print("M ID", a.tag, a.text)
                MAIN_product_data.append(a.text)

        for sub_product in sub_products:
            SUB_product_data, SUB_product_cost = [], []
            for a in sub_product.iter():
                if a.tag == "Quantity":
                    pass
                if a.tag == "ProductIdentification":
                    for b in a.find("PartnerProductIdentification"):
                        print("S INFO", b.tag, b.text)
                        SUB_product_data.append(b.text)
                if a.tag == "UnitListPrice":
                    for b in a.find("FinancialAmount"):
                        print("S COST", b.tag, b.text)
                        SUB_product_cost.append(b.text)
            SUB_products_data.append(SUB_product_data)
            SUB_products_cost.append(SUB_product_cost)
        print(MAIN_product_data)
        print(SUB_products_data)
    w_sheet.append(MAIN_product_data)
    for p in SUB_products_data:
        w_sheet.append(p)
    w_book.save(os.getcwd() + '\\qutation\\tmp\\samples.xlsx')

save_excel()