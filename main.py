from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
PATH = "F:/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()
username.send_keys('123456')
password.send_keys('123456')
login.click()

next1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_ac8f"))
)
next1.click()
time.sleep(2)
next2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))
)
next2.click()
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]'))
)
search.click()

search2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
)
keyword = "#dog"
search2.send_keys(keyword)
search3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]'))
)
search3.click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_aagv"))
)
imgs = driver.find_elements_by_class_name("x5yr21d")
path = os.path.join(keyword)
os.mkdir(path)
count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    wget.download(img.get_attribute("src"), save_as)
    count += 1
