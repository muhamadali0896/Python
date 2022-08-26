# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r'C:\Users\muham\Downloads\chromedriver.exe')
driver.get("https://diswsiemens.service-now.com/csm?id=csm_login")

username = "mohammedali.abdulkadhar@intelizign.com"
password = "CadenceAllowed@2021"

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)

# click login button
driver.find_element_by_name("login").click()

#inputs
sharelink=""
desc="BMIDE Deployment in QA(10.11.100.222)"
users_impacted="10"
app_impact=""
cust_involved=""
expected="Datamodel changes to be deployed successfully."
reproduce='Please deploy the datamodel changes by using the package available in " "\nThe package is available in local(10.11.100.222):D:\BMIDE\04052022'

recent_change=""
urgency=""



WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="xb0928873cb53020000f8d856634c9cb0"]/li[2]/a/span[1]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Case"]/li/a/span'))).click()


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'sp_formfield_short_description'))).send_keys(desc)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'sp_formfield_number_of_impacted'))).send_keys(users_impacted)

# select1=Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'select2-drop"]'))))
# select1.select_by_visible_text("tea")
#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select2-chosen-7"]'))).click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'sp_formfield_expected_behavior'))).send_keys(expected)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'sp_formfield_steps_to_reproduce'))).send_keys(reproduce)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'sp_formfield_description'))).send_keys(reproduce)



