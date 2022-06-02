import pandas as pd
from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\user\Project\LEC-Finder\chromedriver.exe')
url = 'https://ieilms.jbnu.ac.kr/'
driver.get(url)
time.sleep(2)

driver.find_element_by_xpath('//*[@id="id"]').send_keys('202110065')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('allzero5391.')

loginbtn = driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input')
loginbtn.click()
time.sleep(2)

def lec2_quiz():
    driver.get('https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id=27607')
    quizbtn = driver.find_element_by_xpath('//*[@id="center"]/div/b/div/div/div[3]/a')
    quizbtn.click()
    time.sleep(2)
    lecbtn = driver.find_element_by_xpath('//*[@id="treeboxtab"]/div/table/tbody/tr[10]/td[2]/table/tbody/tr/td[4]/span')
    lecbtn.click()
    time.sleep(2)
    # 퀴즈 개수
    elements = driver.find_elements_by_css_selector('#borderB > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 퀴즈 리스트
        title = []
        date = []
        submit = []
        for i in range(2, elementcount+1):
            titleresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[2]'.format(i)).text
            title.append(str(titleresult))
            dateresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[3]'.format(i)).text
            date.append(str(dateresult))
            submitresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[4]'.format(i)).text
            submit.append(str(submitresult))

        dc = pd.DataFrame({'퀴즈제목': title,
                           '기간': date,
                           '제출여부': submit})

        print(dc['기간'].str[24:29])
    else:
        print('퀴즈는 없습니다.')

print(lec2_quiz())