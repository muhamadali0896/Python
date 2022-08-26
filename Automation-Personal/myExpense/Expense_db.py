# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:35:42 2022

@author: muham
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd
from tkinter import *
from  tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure

def create_server_connection(hostname,username,password,db):
    connection = None
    try:
        connection = mysql.connector.connect(host = hostname,user = username,passwd = password,database = db)
        print("MySql database connection successfull")
    except Error as err:
        print(f"Error:'{err}'")
    return connection

def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfull")
    except Error as err:
        print(f"Error:'{err}'")
def read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error:'{err}'")
def get_data_expense():
    connection = create_server_connection("localhost", "root", "","epiz_30279605_homefinance")
    q1 = """
    select day(ExpenseDate),month(ExpenseDate),year(ExpenseDate), ExpenseItem, sum(ExpenseCost) from tblexpense GROUP BY ExpenseDate;
    """
    results = read_query(connection, q1)
    from_db = []
    count=0
    for result in results:
        result = list(result)
        from_db.append(result)
    columns = ["Day","Month","year","Expense","Cost"]
    df = pd.DataFrame(from_db, columns = columns)
    return df 

def get_data_expense_monthwise(month):
    connection = create_server_connection("localhost", "root", "","epiz_30279605_homefinance")
    q1 = """
    select day(ExpenseDate),month(ExpenseDate),year(ExpenseDate), ExpenseItem, sum(ExpenseCost), ExpenseCategory from tblexpense GROUP BY ExpenseDate;
    """
    results = read_query(connection, q1)
    from_db = []
    count=0
    for result in results:
        result = list(result)
        from_db.append(result)
    columns = ["Day","Month","year","Expense","Cost","Category"]
    df = pd.DataFrame(from_db, columns = columns)
    return df 

def get_data_expense_datewise(from_date, to_date):
    connection = create_server_connection("localhost", "root", "","epiz_30279605_homefinance")
    q1 = """
    select day(ExpenseDate),month(ExpenseDate),year(ExpenseDate), ExpenseItem, ExpenseCost, ExpenseCategory from tblexpense where ExpenseDate between '"""+str(from_date)+"""' and '"""+str(to_date)+"""';
    """
    results = read_query(connection, q1)
    from_db = []
    count=0
    for result in results:
        result = list(result)
        from_db.append(result)
    columns = ["Day","Month","year","Expense","Cost","Category"]
    df = pd.DataFrame(from_db, columns = columns)
    return df 










