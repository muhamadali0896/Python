# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:09:17 2022

@author: muham
"""

import Expense_db
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry

result_df = Expense_db.get_data_expense()


df_month = result_df[['Month','Cost']].groupby('Month').sum()
root= tk.Tk()

cal_from=DateEntry(root,selectmode='day')
cal_from.pack(fill = tk.BOTH, expand = True)

cal_to=DateEntry(root,selectmode='day')
cal_to.pack(fill = tk.BOTH, expand = True)

def getChart():
    c_from = cal_from.get_date()
    c_to = cal_to.get_date()
    res_datewise = Expense_db.get_data_expense_datewise(c_from, c_to)
    
    figure = plt.Figure(figsize=(6,5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().pack()
    df_month = res_datewise[['Category','Cost']].groupby('Category').sum()
    df_month.plot(kind='bar', legend=True, ax=ax)
    ax.set_title('Expense Chart')

b1 = tk.Button(root, text = "submit",command=getChart,
            background = "red", fg = "white")
b1.pack(side = tk.TOP, expand = True, fill = tk.BOTH)


root.mainloop()

