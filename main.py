# selenium for web driving
import selenium
from selenium import webdriver
import os
driver = webdriver.Chrome()

# Open the website
driver.get('http://toolsqa.com/automation-practice-form/')
# Locate 
id_box = driver.find_element_by_name('firstname')
pass_box = driver.find_element_by_name('lastname')

print(id_box)
print(pass_box)


