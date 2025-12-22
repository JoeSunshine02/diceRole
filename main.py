#main file for running rolling configuration

#imports
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from helper import *
from WH10thHelper import *

from tkinter import *
from tkinter import ttk

ReqConfig = LoadMasterConfig()
ReqConfig.MasterValidate()

WeaponList = WeaponLoader()
for weapon in WeaponList:
    print(weapon)

TargetList = TargetLoader()
for target in TargetList:
    print(target)

root = Tk()
root.title("Dice roller Ver 0.0")
frm = ttk.Frame(root, padding=(3, 3, 12,12))
frm.grid(column=0, row=0, sticky=(N,W,E,S))

gameTypeLabel = ttk.Label(frm, text = 'Game Type:').grid(column=0,columnspan=2, row=1, sticky=(W))
GameType = ttk.Label(frm, text = ReqConfig.GameType).grid(column=2, row = 1, sticky = (E))

GameSubtypeLabel = ttk.Label(frm,text = 'Game Sub Type').grid(column=0,columnspan=2, row=2, sticky=(W))
GameSubType = ttk.Label(frm,text=ReqConfig.GameSubType).grid(column=2, row=2, sticky=(W,E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
for child in frm.winfo_children():
    child.grid_configure(padx=5, pady=5)
#root.mainloop()