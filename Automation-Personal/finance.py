# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:17:23 2022

@author: muham
"""
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


Window =tkinter.Tk()
Window.title("UI")
Window.geometry('350x200')
Ename = tkinter.StringVar()
Cat = tkinter.StringVar()
Amt = tkinter.StringVar()

LabelName = tkinter.Label(Window, text= "name").grid(row=0)
name = tkinter.Entry(Window,textvariable= Ename).grid(row =0, column=1)

LabelC = tkinter.Label(Window, text= "Category").grid(row=1)
Category = tkinter.ttk.Combobox(Window,textvariable=Cat)
Category['values'] = (' Food','Travel', 'Medical')
Category.grid(row =1, column=1)
Category.current()

labelamt = tkinter.Label(Window, text = "Amount:").grid(row = 2)
Amount = tkinter.Entry(Window,textvariable= Amt).grid(row =2, column=1)


def myTask():
    caps= DesiredCapabilities().CHROME
    caps["pageLoadStragey"] = "eager"
    driver = webdriver.Chrome(desired_capabilities=caps,executable_path=r'C:\Users\muham\Downloads\chromedriver.exe')
    driver.get("http://sumaiyahomefinance.epizy.com/expense1/")
    
    username = "ali"
    password = "ali"

    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/form/fieldset/div[3]/button'))).click()
    
    driver.get("http://sumaiyahomefinance.epizy.com/expense1/add-expense.php")
    
    WebDriverWait(driver, 20).until(EC.((By.XPATH,)
    driver.find_element_by_name("costitem").send_keys(Amt.get())
    
    # WebDriverWait(driver, 5).until()

btn =  tkinter.Button(Window, text = 'Submit !',command=myTask).grid (row=3)
Window.mainloop()

# Window.mainloop()

