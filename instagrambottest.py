#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class InstaBot:
    def loginbot(self,username,password):
        driver.get("https://www.instagram.com/")
        WebDriverWait(driver).until(lambda d: d.find_element_by_name("username"))
        user=driver.find_element_by_name("username")
        user.send_keys(username)
        pw=driver.find_element_by_name("password")
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        

    def clicknotnow(self):
        wait.until(EC.presence_of_element_located(driver.find_element_by_class_name("sqdOP")))
        driver.find_element_by_class_name("sqdOP").click()
    def sendmessage(self,recipient):
        pass
    def folow(self,recipient):
        pass
    def newfollowermessage(self,recipient):
        pass


driver=webdriver.Chrome("C:/Users/Gowri Arunsha/Documents/Work/Web Automation/chromedriver")
wait=WebDriverWait(driver,3)
b=InstaBot()
b.loginbot("username","********")
b.clicknotnow()