import time
import csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# 京东所在网站
driver.get("https://www.jd.com/")

# 输入需要查找的关键字
p_input = driver.find_element_by_id('key')
p_input.send_keys('python编程')  # 找到输入框输入
time.sleep(1)
# 点击搜素按钮
button=driver.find_element_by_class_name("button").click()
time.sleep(1)
all_book_info = []
num=200
head=['书名', '价格', '作者', '出版社']
#csv文件的路径和名字
path='D:/try45/666/python编程.csv'
def write_csv(head,all_book_info,path):
    with open(path, 'w', newline='',encoding='utf-8') as file:
        fileWriter =csv.writer(file)
        fileWriter.writerow(head)
        fileWriter.writerows(all_book_info) 
# 爬取一页
def get_onePage_info(web,num):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    page_text =driver.page_source
    # with open('3-.html', 'w', encoding='utf-8')as fp:
    #     fp.write(page_text)
    # 进行解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//li[contains(@class,"gl-item")]')
    for li in li_list:
        num=num-1
        book_infos = []
        book_name = ''.join(li.xpath('.//div[@class="p-name"]/a/em/text()'))     # 书名
        book_infos.append(book_name)
        price = '￥' + li.xpath('.//div[@class="p-price"]/strong/i/text()')[0]   # 价格
        book_infos.append(price)
        author_span = li.xpath('.//span[@class="p-bi-name"]/a/text()')
        if len(author_span) > 0:  # 作者
            author = author_span[0]
        else:
            author = '无'
        book_infos.append(author)
        store_span = li.xpath('.//span[@class="p-bi-store"]/a[1]/text()')  # 出版社
        if len(store_span) > 0:
            store = store_span[0]
        else:
            store = '无'
        book_infos.append(store)
        all_book_info.append(book_infos)
        if num==0:
            break
    return num

while num!=0:
    num=get_onePage_info(driver,num)
    driver.find_element_by_class_name('pn-next').click()  # 点击下一页
    time.sleep(2)
write_csv(head,all_book_info,path)
driver.close()
