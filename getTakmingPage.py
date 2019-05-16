import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

url = 'http://netinfo.takming.edu.tw/tip/up.php'
driver_main = webdriver.Chrome('/usr/local/bin/chromedriver')
driver_main.get(url)

driver_main.find_element_by_id('Passwd').send_keys('F129931231')
driver_main.find_element('name', 'UserID').send_keys('D10516163')
main_window = driver_main.current_window_handle
driver_main.find_elements_by_name('image')[1].click()
# url = 'http://netinfo.takming.edu.tw/tip/grade/grade_course_list.php'
url = 'http://netinfo.takming.edu.tw/tip/login_xx.php'
driver_main.get(url)
driver_main.switch_to.alert.accept()
driver_main.switch_to_window(main_window)
url = 'http://netinfo.takming.edu.tw/tip/list_fun.php?flag=1&item=08&funitem=&Type=2'
driver_main.get(url)
# driver_main.find_element_by_link_text('http://netinfo.takming.edu.tw/tip/grade/explain.php').click()
driver_main.get('http://netinfo.takming.edu.tw/tip/grade/explain.php')
sleep(2)

# for value, index in linkIndex:
#     if value['href'] == 'grade/explain.php':
#         print(index)

# print(images)
# playload = {
#     'UserID': 'D10516163',
#     'Passwd': 'F129931231'
# }
# session = rq.Session()
#
# r = session.post(url, data=playload)
# cookie = r.cookies.get_dict()
#
# cooke = ''
# for key, value in cookie.items():
#     cooke += key + '=' + value + ';'
#
# header = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Cookie': cooke,
#     'Host': 'netinfo.takming.edu.tw',
#     'Referer': 'http://netinfo.takming.edu.tw/tip/grade/explain.php',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
# }
#
# # 填寫評量頁
# url = 'http://netinfo.takming.edu.tw/tip/grade/grade_course_list.php'
# r = rq.get(url, headers=header)
# html_doc = r.text
# soup = BeautifulSoup(html_doc)
# askPage = soup.select('td a')
# baseUrl = 'http://netinfo.takming.edu.tw/tip/grade/'
# link = []
# for alink in askPage:
#     link.append(baseUrl+alink['href'])
# # print(r.cookies.get_dict())
# print(link)
