import time
import csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# 名言所在网站
driver.get("http://quotes.toscrape.com/js/")
# 所有数据
subjects = []
# 单个数据
subject=[]
#定义csv表头
quote_head=['名言','作者','标签']
#csv文件的路径和名字
quote_path='D:/try45/666/名人名言.csv'
#存放内容的列表

def write_csv(csv_head,csv_content,csv_path):
    with open(csv_path, 'w', newline='',encoding='utf-8') as file:
        fileWriter =csv.writer(file)
        fileWriter.writerow(csv_head)
        fileWriter.writerows(csv_content)       
n = 10
for i in range(0, n):
    driver.find_elements_by_class_name("quote")
    res_list=driver.find_elements_by_class_name("quote")
    # 分离出需要的内容
    for tmp in res_list:
        saying = tmp.find_element_by_class_name("text").text
        author =tmp.find_element_by_class_name("author").text
        tags =tmp.find_element_by_class_name("tags").text
        subject=[]
        subject.append(saying)
        subject.append(author)
        subject.append(tags)
        print(subject)
        subjects.append(subject)
        subject=[]
        write_csv(quote_head,subjects,quote_path)
    print('成功爬取第' + str(i + 1) + '页')
    if i == n-1:
        break
    driver.find_elements_by_css_selector('[aria-hidden]')[-1].click()
    time.sleep(2)
driver.close()
