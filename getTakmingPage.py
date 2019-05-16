import requests as rq
from bs4 import BeautifulSoup

playload = {
    'UserID': 'D10516262',
    'Passwd': 'a31512051'
}
session = rq.Session()
url = 'http://netinfo.takming.edu.tw/tip/login_xx.php'

r = session.post(url, data=playload)
cookie = r.cookies.get_dict()

cooke = ''
for key, value in cookie.items():
    cooke += key + '=' + value + ';'

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': cooke,
    'Host': 'netinfo.takming.edu.tw',
    'Referer': 'http://netinfo.takming.edu.tw/tip/grade/explain.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

# 填寫評量頁
url = 'http://netinfo.takming.edu.tw/tip/grade/grade_course_list.php'
r = rq.get(url, headers = header)
html_doc = r.text
soup = BeautifulSoup(html_doc)
#
# print(r.cookies.get_dict())
print(soup.prettify())
