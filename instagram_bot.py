'''
 * @channel Morita DataLand
 * @author Morita Tarvirdians
 * @email tarvirdians.morita@gmail.com
 * @desc Instagram Bot using Selenium and Python
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import data
from time import sleep


DRIVER_PATH = r"C:\\Program Files (x86)\\chromedriver.exe"

# chrome options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

class Bot():
    def __init__(self, username, password) -> None:
        self.driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)
        self.driver.get('https://www.instagram.com/')
        sleep(3)
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_xpath('//div[text() = "Log In"]').click()


    def user_info(self, user_id):
        search = self.driver.find_element_by_xpath('//span[text()="Search"]')
        search.click()
        sleep(5)
        search1 = self.driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search1.send_keys(user_id)
        sleep(10)
        search1.send_keys(Keys.ENTER)
        sleep(1)
        search1.send_keys(Keys.ENTER)
        sleep(10)
        followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span')
        followings = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span')
        print("follower count:  ", followers.text)
        print("following count: ", followings.text)
        self.driver.close()


insta_bot = Bot("morita_dataland", data.password)
sleep(15)
insta_bot.user_info("zuch")