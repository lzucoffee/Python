import requests
from bs4 import BeautifulSoup
import xlsxwriter

def get_book_name(url):
    book_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,'html.parser')
    for book_text in soup.findAll('div',{'class':"pl2"}):
        book_name = book_text.findChildren()[0]
        clean_book_name=book_name.get('title')
        book_list.append(clean_book_name)
    return book_list

final_book_list = []

for page in range(0,250,25):
    final_book_list.extend(get_book_name('https://book.douban.com/top250?start='+ str(page)))

workbook = xlsxwriter.Workbook('豆瓣读书Top250.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'序号')
worksheet.write(0,1,'书名')
row = 1
col = 0

for item in final_book_list:
    worksheet.write(row,col,row-1)
    worksheet.write(row, col+1, item)
    row += 1
workbook.close()







