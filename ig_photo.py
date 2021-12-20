from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget #下載東西



path="C:/Users/acer/Desktop/chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://www.instagram.com/")


username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
loging=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
username.clear()
password.clear()
username.send_keys("12345")
password.send_keys("54321")
loging.click()

search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    )
keyword="#曼赤肯"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    )
imgs=driver.find_elements_by_class_name("FFVAD")

path=os.path.join(keyword)
os.mkdir(path) #創建資料夾

count=0
for img in imgs:
    save_as=os.path.join(path,keyword+str(count)+".jpg")
    print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"),save_as) #(取得照片的位置,存哪裡)
    count+=1
