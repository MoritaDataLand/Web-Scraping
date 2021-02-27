'''
 * @channel Morita DataLand
 * @author Morita Tarvirdians
 * @email tarvirdians.morita@gmail.com
 * @desc Web Scraping With Selenium
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver_path = r"C:\\Program Files (x86)\\chromedriver.exe"

# chrome options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])



driver = webdriver.Chrome(driver_path, chrome_options=options)
#driver.get("https://google.com")

# get url
url = "https://www.mastersportal.com/"
driver.get(url)

# locate HomeWhat element in the page and send keys to it
what_search_box = driver.find_element_by_id("HomeWhat")
what_search_box.send_keys("computer")
what_search_box.send_keys(Keys.ENTER)

# locate HomeWhere element in the page and send keys to it
where_search_box = driver.find_element_by_id("HomeWhere")
where_search_box.send_keys("Germany")
where_search_box.send_keys(Keys.ENTER)

time.sleep(5)

#get some fields and write them in the csv file
lst = []
cols = ["title", "uni", "fee"]
titles = driver.find_elements_by_class_name("StudyTitle")
unis = driver.find_elements_by_class_name("LocationFact:nth-child(1)")
fees = driver.find_elements_by_class_name("KeyFact:nth-child(1)")

for (title, uni, fee) in (zip(titles, unis, fees)):
    lst.append((title.text, uni.text, fee.text))

driver.quit()

df = pd.DataFrame(lst, columns=cols )

df.to_csv("out.csv")
 


