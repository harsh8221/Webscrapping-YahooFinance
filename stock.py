from company_class import Company
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import math

class Stock:
    def __init__(self,name,url,no_of_purchase):
        self.name=name
        self.url=url
        self.no_of_purchase=no_of_purchase
        self.stack=[]
        self.value_stack=[]


def earning_of_portfolio():
    arr = getPortfolio()
    earning=0
    investment=0
    for item in arr:
        share=0
        invest=0
        for i in range(item.no_of_purchase):
            invest+=item.stack[i]*item.value_stack[i]
            share += item.stack[i]
        c1 = Company(item.url)
        c1.getStock()
        earning += share*c1.value
        investment+=invest
        print(item.name + " " + str(share*c1.value)+ " " + str(invest)+ " " + str(share*c1.value - invest))
    
    print(str(earning) + " " + str(investment))
    return earning-investment


def add_new_company():
    url = input("Enter the Yahoo finanace url of company you want to add\n")
    c1 = Company(url)
    c1.getStock()
    file_path = 'first.xls'
    read = open_workbook(file_path,formatting_info=True)
    read_sheet = read.sheet_by_index(0)
    wr = copy(read)
    wr_sheet = wr.get_sheet(0)
    i = math.floor(read_sheet.cell_value(0,0))
    i+=1
    wr_sheet.write(i,0,c1.name)
    wr_sheet.write(i,1,c1.url)
    wr_sheet.write(i,2,0)
    wr_sheet.write(0,0,i)
    wr.save(file_path)
    print(c1.name)


def getPortfolio():
    file_path = 'first.xls'
    read = open_workbook(file_path,formatting_info=True)
    read_sheet = read.sheet_by_index(0)
    n = read_sheet.cell_value(0,0)
    c1 = Stock("","",0)
    arr = []
    n = math.floor(n)
    for i in range(n):
        c1.name = read_sheet.cell_value(i+1,0)
        c1.url = read_sheet.cell_value(i+1,1)
        c1.no_of_purchase = math.floor(read_sheet.cell_value(i+1,2))
        arr.append(Stock(c1.name,c1.url,c1.no_of_purchase))
        for j in range(c1.no_of_purchase):
            arr[i].stack.append(math.floor(read_sheet.cell_value(i+1,j*2+3)))
            arr[i].value_stack.append(read_sheet.cell_value(i+1,j*2+4))       

    return arr


def add_new_stack(arr):
    print("Give the number of the company you have in your portfolio.")
    j=1
    for i in arr:
        print(str(j) + " " + i.name)
        j+=1
    q = int(input(),10)
    nos = input("Number of share of company " + arr[q-1].name + " : ")
    apo = input("At what price you bought " + str(nos) + " of share of company " + arr[q-1].name + " : ")
    file_path = "first.xls"
    nos = int(nos,10)
    apo = float(apo)
    read = open_workbook(file_path)
    read_sheet = read.sheet_by_index(0)
    wr = copy(read)
    wr_sheet = wr.get_sheet(0)
    y = math.floor(read_sheet.cell_value(q,2))
    wr_sheet.write(q,y*2 + 3,nos)
    wr_sheet.write(q,y*2 + 4,apo)
    wr_sheet.write(q,2,y+1)
    wr.save(file_path)
    arr[q-1].stack.append(nos)
    arr[q-1].value_stack.append(apo)


def showPortfolio():
    arr = getPortfolio()
    for item in arr:
        print(item.name + " : " + str(item.no_of_purchase))
        for i in range(item.no_of_purchase):
            print(str(item.stack[i]) + " " + str(item.value_stack[i]))



want=-1
while want!=0:
    print("1 Show Portfolio")
    print("2 Add new stock")
    print("3 Add new stack in existing company")
    print("4 Profit/loss")
    if want==1:
        showPortfolio()
    elif want==2:
        try:
            add_new_company()
        except:
            print("Adding of new company is falied")
    elif want==3:
        arr=getPortfolio()
        add_new_stack(arr)
    elif want==4:
        earning = earning_of_portfolio()
        print(earning)
