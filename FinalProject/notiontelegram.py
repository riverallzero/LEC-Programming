import telegram
from telegram.ext import Updater, MessageHandler
from telegram.ext import Filters
import lecfinder as lf
from selenium import webdriver
import time


token = '5513740361:AAHKlEFGN8ySC7dLpkThZF4-XjnOjus-mSQ'
id = '5580001250'
bot = telegram.Bot(token=token)


# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "할일":  # 사용자가 보낸 메세지가 "할일"이면
        bot.send_message(chat_id=id, text='로딩중∙∙∙')
        driver = webdriver.Chrome(r'C:\Pych.Projects\Project\chromedriver.exe')
        url = 'https://ieilms.jbnu.ac.kr/'
        driver.get(url)
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="id"]').send_keys('202110065')
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('allzero5391.')

        loginbtn = driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input')
        loginbtn.click()
        time.sleep(2)

        report1 = lf.report1_result(driver)
        report2 = lf.report2_result(driver)
        video1 = lf.video1_result(driver)
        video2 = lf.video2_result(driver)
        quiz1 = lf.quiz1_result(driver)
        quiz2 = lf.quiz2_result(driver)

        if report1 and report2 == '레포트는 없습니다.':
            bot.send_message(chat_id=id, text='[레포트] 완료')
        else:
            if report1 != '레포트는 없습니다.':
                send_telegram_msg(report1)
                bot.send_message(chat_id=id, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27306')
            elif report2 != '레포트는 없습니다.':
                send_telegram_msg(report2)
                bot.send_message(chat_id=id, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27607')

        if quiz1 and quiz2 == '퀴즈는 없습니다.':
            bot.send_message(chat_id=id, text='[퀴즈] 완료')
        else:
            if quiz1 != '퀴즈는 없습니다.':
                send_telegram_msg(quiz1)
                bot.send_message(chat_id=id, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27306')
            elif quiz2 != '퀴즈는 없습니다.':
                send_telegram_msg(quiz2)
                bot.send_message(chat_id=id, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27607')


        if video1 and video2 == '영상은 없습니다.':
            bot.send_message(chat_id=id, text='[강의 영상] 완료')
        else:
            if video1 != '영상은 없습니다.':
                send_telegram_msg(video1)
                bot.send_message(chat_id=id, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27306')
            elif video2 != '영상은 없습니다.':
                send_telegram_msg(video2)
                bot.send_message(chat_id=id, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id=27607')

        logout = driver.find_element_by_xpath('//*[@id="centerTop"]/div[2]/ul/li/div/a[4]')
        logout.click()
        time.sleep(2)

def send_telegram_msg(report2):
    if isinstance(report2, tuple):
        bot.send_message(chat_id=id, text='{} (기한:{})'.format(report2[0], report2[1]))
    else:
        bot.send_message(chat_id=id, text='{}'.format(report2))


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
