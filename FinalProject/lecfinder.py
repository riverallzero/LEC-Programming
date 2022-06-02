import pandas as pd
from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Pych.Projects\Project\chromedriver.exe')
url = 'https://ieilms.jbnu.ac.kr/'
driver.get(url)
time.sleep(2)

driver.find_element_by_xpath('//*[@id="id"]').send_keys('202110065')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('allzero5391.')

loginbtn = driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input')
loginbtn.click()
time.sleep(2)

# lec 1 = 매스컴, lec 2 = K-food
def lec1_report():
    driver.get('https://ieilms.jbnu.ac.kr/paper/paperList.jsp')
    lecbtn = driver.find_element_by_xpath('//*[@id="treebox"]/div/table/tbody/tr[11]/td[2]/table/tbody/tr/td[4]/span') # 매스컴
    lecbtn.click()
    time.sleep(2)
    # 레포트 개수
    elements = driver.find_elements_by_css_selector('#borderB > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 레포트 리스트
        title = []
        date = []
        submit = []
        ending = []
        for i in range(2, elementcount+1):
            titleresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[2]'.format(i)).text
            title.append(str(titleresult))
            dateresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[3]'.format(i)).text
            date.append(str(dateresult))
            submitresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[4]'.format(i)).text
            submit.append(str(submitresult))
            endingresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[5]'.format(i)).text
            ending.append(str(endingresult))

        df = pd.DataFrame({'과제제목': title,
                           '제출기간': date,
                           '제출여부': submit})

        return df
    else:
        return '매스컴 레포트는 없습니다.'


def lec2_report():
    driver.get('https://ieilms.jbnu.ac.kr/paper/paperSelectGroup.jsp')
    lecbtn = driver.find_element_by_xpath('//*[@id="treebox"]/div/table/tbody/tr[10]/td[2]/table/tbody/tr/td[4]/span') # K-food
    lecbtn.click()
    time.sleep(2)
    # 레포트 개수
    elements = driver.find_elements_by_css_selector('#borderB > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 레포트 리스트
        title = []
        date = []
        submit = []
        ending = []
        for i in range(2, elementcount+1):
            titleresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[2]'.format(i)).text
            title.append(str(titleresult))
            dateresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[3]'.format(i)).text
            date.append(str(dateresult))
            submitresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[4]'.format(i)).text
            submit.append(str(submitresult))
            endingresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[5]'.format(i)).text
            ending.append(str(endingresult))

        df = pd.DataFrame({'과제제목': title,
                           '제출기간': date,
                           '제출여부': submit})
        return df
    else:
        return 'k-food 레포트는 없습니다.'


def lec1_video():
    driver.get('https://ieilms.jbnu.ac.kr/attend/videoDataViewAttendListStudent.jsp')
    lecbtn = driver.find_element_by_xpath('//*[@id="center"]/div/b/div/div/div[3]/a')
    lecbtn.click()
    time.sleep(2)
    videobtn = driver.find_element_by_xpath('//*[@id="treeboxtab"]/div/table/tbody/tr[19]/td[2]/table/tbody/tr/td[4]/span')
    videobtn.click()
    time.sleep(2)
    # 비디오 개수
    elements = driver.find_elements_by_css_selector('#dataBox > table > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 비디오 리스트
        title = []
        date = []
        percent = []
        attendence = []
        for i in range(2, elementcount+1):
            titleresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[2]'.format(i)).text
            title.append(str(titleresult))
            dateresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[3]'.format(i)).text
            date.append(str(dateresult))
            percentresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[5]'.format(i)).text
            percent.append(str(percentresult))
            attendenceresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[6]'.format(i)).text
            attendence.append(str(attendenceresult))

        ds = pd.DataFrame({'강의제목': title,
                           '인정기간': date,
                           '출석여부': attendence})

        return ds

    else:
        return '매스컴 강의는 없습니다.'


def lec2_video():
    driver.get('https://ieilms.jbnu.ac.kr/attend/videoDataViewAttendListStudent.jsp')
    lecbtn = driver.find_element_by_xpath('//*[@id="center"]/div/b/div/div/div[3]/a')
    lecbtn.click()
    time.sleep(2)
    videobtn = driver.find_element_by_xpath('//*[@id="treeboxtab"]/div/table/tbody/tr[20]/td[2]/table/tbody/tr/td[4]/span')
    videobtn.click()
    time.sleep(2)
    # 비디오 개수
    elements = driver.find_elements_by_css_selector('#dataBox > table > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 비디오 리스트
        title = []
        date = []
        percent = []
        attendence = []
        for i in range(2, elementcount+1):
            titleresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[2]'.format(i)).text
            title.append(str(titleresult))
            dateresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[3]'.format(i)).text
            date.append(str(dateresult))
            percentresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[5]'.format(i)).text
            percent.append(str(percentresult))
            attendenceresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[6]'.format(i)).text
            attendence.append(str(attendenceresult))

        ds = pd.DataFrame({'강의제목': title,
                           '인정기간': date,
                           '출석여부': attendence})

        return ds

    else:
        return 'k-food 강의는 없습니다.'


def lec1_quiz():
    driver.get('https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id=27306')
    quizbtn = driver.find_element_by_xpath('//*[@id="center"]/div/b/div/div/div[3]/a')
    quizbtn.click()
    time.sleep(2)
    lecbtn = driver.find_element_by_xpath('//*[@id="treeboxtab"]/div/table/tbody/tr[11]/td[2]/table/tbody/tr/td[4]/span')
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
            if not titleresult:
                continue
            else:
                title.append(str(titleresult))
            dateresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[3]'.format(i)).text
            if not dateresult:
                continue
            else:
                date.append(str(dateresult))
            submitresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[4]'.format(i)).text
            if not titleresult:
                continue
            else:
                submit.append(str(submitresult))

        dc = pd.DataFrame({'퀴즈제목': title,
                           '기간': date,
                           '제출여부': submit})

        return dc
    else:
        return '매스컴 퀴즈는 없습니다.'


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

        return dc
    else:
        return 'K-food 퀴즈는 없습니다.'


def report1_result():
    df = lec1_report()
    if isinstance(df, str):
        return '매스컴 레포트는 없습니다.'
    else:
        count = len(df['과제제목'])
        for s in range(count):
            if df['제출여부'][s] == '미제출':
                return df['과제제목'][s], 'https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27306'
        return '매스컴 레포트는 없습니다.'


def report2_result():
    df = lec2_report()
    if isinstance(df, str):
        return 'k-food 레포트는 없습니다.'
    else:
        count = len(df['과제제목'])
        for s in range(count):
            if df['제출여부'][s] == '미제출':
                return df['과제제목'][s], 'https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27607'
        return 'k-food 레포트는 없습니다.'


def video1_result():
    ds = lec1_video()
    if isinstance(ds, str):
        return '매스컴 영상은 없습니다.'
    else:
        count = len(ds['강의제목'])
        for s in range(count):
            if ds['출석여부'][s] == '결석':
                return ds['강의제목'][s], 'https://ieilms.jbnu.ac.kr/mypage/data/dataList.jsp?group_id=27306'
        return '매스컴 영상은 없습니다.'


def video2_result():
    ds = lec2_video()
    if isinstance(ds, str):
        return 'k-food 영상은 없습니다.'
    else:
        count = len(ds['강의제목'])
        for s in range(count):
            if ds['출석여부'][s] == '결석':
                return ds['강의제목'][s], 'https://ieilms.jbnu.ac.kr/mypage/data/dataList.jsp?group_id=27607'
        return 'k-food 영상은 없습니다.'


def quiz1_result():
    dc = lec1_quiz()
    if isinstance(dc, str):
        return '매스컴 퀴즈는 없습니다.'
    else:
        count = len(dc['퀴즈제목'])
        for s in range(count):
            if dc['제출여부'][s] == '미제출':
                return dc['퀴즈제목'][s], 'https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id=27306'
        return '매스컴 퀴즈는 없습니다.'


def quiz2_result():
    dc = lec2_quiz()
    if isinstance(dc, str):
        return 'k-food 퀴즈는 없습니다.'
    else:
        count = len(dc['퀴즈제목'])
        for s in range(count):
            if dc['제출여부'][s] == '미제출':
                return dc['퀴즈제목'][s], 'https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id=27607'
        return 'k-food 퀴즈는 없습니다.'
