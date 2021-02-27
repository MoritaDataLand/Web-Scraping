'''
 * @channel Morita DataLand
 * @author Morita Tarvirdians
 * @email tarvirdians.morita@gmail.com
 * @desc Web Scraping With Selenium
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = r"C:\\Program Files (x86)\\chromedriver.exe"

# chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# set driver
driver = webdriver.Chrome(driver_path, chrome_options=options)

# get url
url = "https://www.mastersportal.com/"
driver.get(url)

# element = driver.find_element_by_id("LoginButton")
# element.click()
try:
    driver.execute_script("window.scrollTo(0,1000)")
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "TakeTest"))
    )
    element.click()
    time.sleep(3)
    driver.get_screenshot_as_file("screenshot.png")
    driver.back()
    
except:
    driver.quit()
