from telnetlib import EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import re
import urllib.request
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = webdriver.ChromeOptions()
chromeOptions.headless = False           #for headless mode

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe", options=chromeOptions)
chromeOptions = webdriver.ChromeOptions()
driver.set_window_size(1024, 600)
driver.maximize_window()

driver.get("https://pizzaonline.dominos.co.in/menu")

def login_details():
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]").click()
    time.sleep(3)
    mobile = driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input")
    mobile.send_keys("8688424757")
    driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input").click()
    time.sleep(5)
    print("Enter 6 digit otp sent to given mobile number")
    otp = input()
    otp_input = driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input")
    otp_input.send_keys(otp)
    time.sleep(5)
    driver.find_elements_by_xpath("//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button").click()
    time.sleep(7)



def order_food():
    #driver.get("https://pizzaonline.dominos.co.in/menu")
    #time.sleep(5)

    #find pizza and click customize
    driver.find_element_by_xpath("//*[@id='mn-lft']/div[6]/div/div[1]/div/div/div[1]/div/div[6]/button").click()
    time.sleep(3)
    #set to cheese burst and add to cart
    driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/ul/li[3]/div").click()
    driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div[4]/div/div[2]/button").click()
    time.sleep(3)

    #find pizza and click customize
    driver.find_element_by_xpath("//*[@id='mn-lft']/div[6]/div/div[4]/div/div/div[1]/div/div[6]/button").click()
    time.sleep(3)
    #set to cheese burst and add to cart
    driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/ul/li[3]/div").click()
    driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div[4]/div/div[2]/button").click()
    time.sleep(3)
    #make no of pizzas = 2
    driver.find_element_by_xpath("//*[@id='mn-lft']/div[6]/div/div[4]/div/div/div[2]/div[3]/div/div[2]").click()

    #find drumsticks and set to 2
    driver.find_element_by_xpath("//*[@id='mn-lft']/div[16]/div/div[4]/div/div/div[2]/div[2]/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='mn-lft']/div[16]/div/div[4]/div/div/div[2]/div[2]/div/div[2]").click()

     #find dips and set to 2
    driver.find_element_by_xpath("//*[@id='mn-lft']/div[16]/div/div[5]/div/div/div[2]/div[2]/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='mn-lft']/div[16]/div/div[5]/div/div/div[2]/div[2]/div/div[2]").click()

    #checkout
    driver.find_element_by_xpath("//*[@id='__next']/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
    time.sleep(5)



def set_location():
    driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/div/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/button").click()
    time.sleep(5)






#login_details()
order_food()
set_location()