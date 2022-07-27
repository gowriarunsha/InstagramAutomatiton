#importing webdriver package from selenium (installed using pip)
from selenium import webdriver
#for using keyboard keys
from selenium.webdriver.common.keys import Keys
#thread ish
from time import sleep

driver=webdriver.Chrome("C:/Users/Gowri Arunsha/Documents/Work/Web Automation/chromedriver")

driver.get("https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet")
driver.maximize_window()
#wait for website to load
sleep(2)
#find element by xpath
login=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
login.send_keys("username")
#find element by name
pw=driver.find_element_by_name("password")
pw.send_keys("********")
pw.send_keys(Keys.RETURN)
sleep(3)
#clicking not now
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').send_keys(Keys.ENTER)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').send_keys(Keys.ENTER)
sleep(1)


u="username"
user="https://www.instagram.com/"+u
driver.get(user)
driver.find_element_by_class_name("sqdOP").click()
sleep(3)
mess=driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
mess.send_keys("this is an automated message. be happy for me :) sheriyenna")
sleep(1)
mess.send_keys(Keys.ENTER)

sleep(3)
driver.quit()