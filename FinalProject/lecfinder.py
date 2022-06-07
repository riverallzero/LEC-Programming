import pandas as pd
import time

# lec 1 = 매스컴, lec 2 = K-food
def lec1_report(driver):
    # 레포트 사이트 group_id 포함된 url
    driver.get('https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27306')

    # 레포트 개수
    elements = driver.find_elements_by_css_selector('#borderB > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 레포트 리스트
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
            endingresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[5]'.format(i)).text
            ending.append(str(endingresult))

        df = pd.DataFrame({'과제제목': title,
                           '제출기간': date,
                           '제출여부': submit})

        return df
    else:
        return '레포트는 없습니다.'


def lec2_report(driver):
    # 레포트 사이트 group_id 포함된 url
    driver.get('https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27607')

    # 레포트 개수
    elements = driver.find_elements_by_css_selector('#borderB > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 레포트 리스트
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
            endingresult = driver.find_element_by_xpath('//*[@id="borderB"]/tbody/tr[{}]/td[5]'.format(i)).text
            ending.append(str(endingresult))

        df = pd.DataFrame({'과제제목': title,
                           '제출기간': date,
                           '제출여부': submit})
        return df
    else:
        return '레포트는 없습니다.'


def lec1_video(driver):
    # 영상 출석 사이트 group_id 포함된 url
    driver.get('https://ieilms.jbnu.ac.kr/attend/videoDataViewAttendListStudent.jsp?group_id=27306')

    # 비디오 개수
    elements = driver.find_elements_by_css_selector('#dataBox > table > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 비디오 리스트
        title = []
        date = []
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
        return '강의는 없습니다.'


def lec2_video(driver):
    # 영상 출석 사이트 group_id 포함된 url
    driver.get('https://ieilms.jbnu.ac.kr/attend/videoDataViewAttendListStudent.jsp?group_id=27607')

    # 비디오 개수
    elements = driver.find_elements_by_css_selector('#dataBox > table > tbody > tr')
    elementcount = len(elements)
    if elementcount >= 3:
        # 비디오 리스트
        title = []
        date = []
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
        return '강의는 없습니다.'


def lec1_quiz(driver):
    # 퀴즈 사이트 group_id 포함된 url
    driver.get('https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id=27306')

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
        return '퀴즈는 없습니다.'


def lec2_quiz(driver):
    # 퀴즈 사이트 group_id 포함된 url
    driver.get('https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id=27607')

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
        return '퀴즈는 없습니다.'


def report1_result(driver):
    df = lec1_report(driver)
    if isinstance(df, str):
        return '레포트는 없습니다.'
    else:
        count = len(df['과제제목'])
        for s in range(count):
            if df['제출여부'][s] == '미제출':
                return df['과제제목'][s], df['제출기간'].str[24:29][s]
        return '레포트는 없습니다.'


def report2_result(driver):
    df = lec2_report(driver)
    if isinstance(df, str):
        return '레포트는 없습니다.'
    else:
        count = len(df['과제제목'])
        for s in range(count):
            if df['제출여부'][s] == '미제출':
                return df['과제제목'][s], df['제출기간'].str[24:29][s]
        return '레포트는 없습니다.'


def video1_result(driver):
    ds = lec1_video(driver)
    if isinstance(ds, str):
        return '영상은 없습니다.'
    else:
        count = len(ds['강의제목'])
        for s in range(count):
            if ds['출석여부'][s] == '결석':
                return ('매스컴 '+ds['강의제목'][s][9:13]+' 강의'), ds['인정기간'].str[24:29][s]
        return '영상은 없습니다.'


def video2_result(driver):
    ds = lec2_video(driver)
    if isinstance(ds, str):
        return '영상은 없습니다.'
    else:
        count = len(ds['강의제목'])
        for s in range(count):
            if ds['출석여부'][s] == '결석':
                return ('K-Food '+ds['강의제목'][s][0:5]+' 강의'), ds['인정기간'].str[24:29][s] # 강의 제목에서 몇 주차 강의인지
        return '영상은 없습니다.'


def quiz1_result(driver):
    dc = lec1_quiz(driver)
    if isinstance(dc, str):
        return '퀴즈는 없습니다.'
    else:
        count = len(dc['퀴즈제목'])
        for s in range(count):
            if dc['제출여부'][s] == '미제출':
                return dc['퀴즈제목'][s], dc['기간'].str[24:29][s]
        return '퀴즈는 없습니다.'


def quiz2_result(driver):
    dc = lec2_quiz(driver)
    if isinstance(dc, str):
        return '퀴즈는 없습니다.'
    else:
        count = len(dc['퀴즈제목'])
        for s in range(count):
            if dc['제출여부'][s] == '미제출':
                return dc['퀴즈제목'][s], dc['기간'].str[24:29][s]
        return '퀴즈는 없습니다.'
