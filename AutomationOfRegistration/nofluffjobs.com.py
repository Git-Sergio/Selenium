#source selenium_env/bin/activate
#python nofluffjobs.com.py
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math
import time
import os

# Open the page "input(insert link to command line)"
link = input("'Please insert the vacancy link for the site - nofluffjobs.com:'")
driver = webdriver.Chrome()
driver.get(link)
driver.implicitly_wait(10)

#ClickButton "Apply"
driver.find_element_by_css_selector(".btn-primary").click()
driver.implicitly_wait(2)

#ClickButton "Apply without signing in"
button = driver.find_element_by_css_selector(".btn-primary")
button.click()
driver.implicitly_wait(2)

#Insert "Name & Surname"
input1 = driver.find_element_by_css_selector('#name')
input1.send_keys("James Bond")
driver.implicitly_wait(2)

#Insert "E-mail address"
input2 = driver.find_element_by_css_selector("#email")
input2.send_keys("james.bond@gmail.com")
driver.implicitly_wait(2)

# Download file CV
# The path to where to download the file "Upload CV"
button = driver.find_element_by_css_selector("input[type=file]")
# The full path from which the file was downloaded "the root of the program"
current_dir = os.path.abspath(os.path.dirname(__file__))
# Add a file name to this path "Name file.expansion"
file_path = os.path.join(current_dir, "YourCV.pdf")
button.send_keys(file_path)
# button.click(file_path)
print(os.path.abspath(__file__))
driver.implicitly_wait(5)

#ClickButton "cookie"
driver.find_element_by_css_selector(".btn.btn-cookie-blue").click()
driver.implicitly_wait(2)

#Click "Tell even more about yourself"
pointer = driver.find_element_by_css_selector("p.pointer")
pointer.click()
driver.implicitly_wait(5)

# We read the text from the file, and send the text to the field "Message"
a = open("file.txt")
message = driver.find_element_by_css_selector("#message")
message.send_keys(a.read())