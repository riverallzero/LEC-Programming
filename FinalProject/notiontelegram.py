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

driver = webdriver.Chrome(r'C:\Pych.Projects\Project\chromedriver.exe')
url = 'https://ieilms.jbnu.ac.kr/'
driver.get(url)
time.sleep(2)

driver.find_element_by_xpath('//*[@id="id"]').send_keys('202110065')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('allzero5391.')

loginbtn = driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input')
loginbtn.click()
time.sleep(2)

def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "할일":  # 사용자가 보낸 메세지가 "할일"이면
        bot.send_message(chat_id=id, text='로딩중∙∙∙')
        report1 = lf.report1_result(driver)
        report2 = lf.report2_result(driver)
        video1 = lf.video1_result(driver)
        video2 = lf.video2_result(driver)
        quiz1 = lf.quiz1_result(driver)
        quiz2 = lf.quiz2_result(driver)

        bot.send_message(chat_id=id, text='{}\n{}'.format(report1, report2))
        bot.send_message(chat_id=id, text='{}\n{}'.format(video1, video2))
        bot.send_message(chat_id=id, text='{}\n{}'.format(quiz1, quiz2))

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
