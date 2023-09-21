from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Sample:
  def login(self):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.booking.com/")
    driver.maximize_window()
    # driver.find_element(By.XPATH,"//div[@class='ab6cf2edce hero-banner-wrapper b36dba3aaa a2893870c6']").click()
    time.sleep(3)
    city = driver.find_element(By.XPATH,"//input[@name='ss']")
    city.click()
    city.sendKeys("ahemdabad")
    time.sleep(3)
    Checkin_date = driver.find_element(By.XPATH, "//button[@data-testid='date-display-field-start']")
    Checkin_date.click()
    time.sleep(3)
    selectdate = driver.find_element(By.XPATH, "//span[@data-date='2023-07-05']")
    selectdate.click()
    time.sleep(3)
    checkout_date =driver.find_element(By.XPATH,"//button[@class='d47738b911 e246f833f7 fe211c0731'][2]")
    checkout_date.click()
    time.sleep(3)
    selectdate2 = driver.find_element(By.XPATH, "//span[@data-date='2023-07-20']").click()
    searchbutton = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)



obj=Sample()
obj.login()
