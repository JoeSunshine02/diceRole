#main file for running rolling configuration

#imports
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from helper import *
from WH10thHelper import *

#from tkinter import *
#from tkinter import ttk

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

ReqConfig = LoadMasterConfig()
ReqConfig.MasterValidate()

dpg.create_context()
dpg.create_viewport(title='DiceRole', width=800, height=600)
with dpg.window(tag = "DiceRole" ):
    with dpg.menu(label = "Menu"):
        #dpg.add_menu(label = "Menu")
        #dpg.add_text("additional menu options coming soon")
        dpg.add_menu_item(label="Exit", callback=KillMain)
    
    dpg.add_text("Welcome to the generic dice roller. The following Config has been loaded.")
    dpg.add_text(f"Game Type: {ReqConfig.GameType}")
    dpg.add_text(f"Game Edition: {ReqConfig.GameSubType}")
    with dpg.child_window(width=1200, height=400, tag = "RollParent"):
        # master config has been loaded, interprite master config and load profile.
        dpg.add_text("load profile")

       
        WeaponList = MasterLoader(ReqConfig,"Weapon", False, "WeaponParent")
        MasterElementDisplay(WeaponList,"Weapon", ReqConfig.GameType, False)
        
        TargetList = MasterLoader(ReqConfig,"Target", False, "TargetParent")
        MasterElementDisplay(TargetList,"Target",ReqConfig.GameType, False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("DiceRole", True)
dpg.start_dearpygui()
dpg.destroy_context()