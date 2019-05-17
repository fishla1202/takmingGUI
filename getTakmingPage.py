# -*- coding: utf-8 -*-
from selenium import webdriver


def auto_click_takming_page(name, passwd, local):

    # 登入頁
    url = 'http://netinfo.takming.edu.tw/tip/up.php'
    # 開啟網頁模擬器
    try:
        driver_main = webdriver.Chrome(local)
        driver_main.get(url)

        driver_main.find_element_by_id('Passwd').send_keys(passwd)
        driver_main.find_element('name', 'UserID').send_keys(name)
        main_window = driver_main.current_window_handle
        driver_main.find_elements_by_name('image')[1].click()
        url = 'http://netinfo.takming.edu.tw/tip/login_xx.php'
        driver_main.get(url)
        driver_main.switch_to.alert.accept()
        driver_main.switch_to_window(main_window)
        url = 'http://netinfo.takming.edu.tw/tip/list_fun.php?flag=1&item=08&funitem=&Type=2'
        driver_main.get(url)
        driver_main.get('http://netinfo.takming.edu.tw/tip/grade/explain.php')
        driver_main.find_element_by_tag_name('a').click()
        try:
            hasClass = driver_main.find_element_by_tag_name('a')
            while hasClass:
                hasClass.click()
                for i in range(2, 9):
                    d = 2
                    p_index = 1
                    index = ''
                    if i > 7:
                        for k in range(8, 26):
                            if k == 22:
                                d = 2
                                p_index = 5
                            elif k == 19:
                                d = 2
                                p_index = 4
                            elif k == 16:
                                d = 2
                                p_index = 3
                            elif k == 12:
                                d = 2
                                p_index = 2
                            index = '/html/body/form[1]/p[' + str(p_index) + ']/table/tbody/tr[' + str(d) + ']/td[3]/input'
                            driver_main.find_element_by_xpath(index).click()
                            d += 1
                    else:
                        index = '/html/body/form[1]/table/tbody/tr[' + str(i) + ']/td[5]/input'
                        driver_main.find_element_by_xpath(index).click()

                driver_main.find_element_by_xpath("//input[@type='SUBMIT' and @value='送出此表']").click()
                driver_main.find_element_by_tag_name('a').click()
                hasClass = driver_main.find_element_by_tag_name('a')
        except:
            print('doen')
    except:
        print('error driver local')
