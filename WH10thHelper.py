#contains classes for WH10th SubType
import json 
import helper
import dearpygui.dearpygui as dpg

#weapon class
class Weapon:
    numData = 8
    #constructor
    def __init__(self, 
                 WepName, 
                 WepDesc, 
                 WepSkill,
                 WepStrength,
                 WepAP, 
                 WepDamage,
                 WepAttacks = 0,
                 WepKeyWord =[]
                ):
        
        self.Name = WepName
        self.Desc = WepDesc
        self.WepSkill = WepSkill
        self.WepStrength = WepStrength
        self.WepAP = WepAP
        self.WepDamage = WepDamage
        self.WepAttacks = WepAttacks
        self.WepKeyword = WepKeyWord

    #Str print out
    def __str__(self):
        return f"""WepName: {self.Name}: {type(self.Name)}
            WepDesc: {self.Desc}: {type(self.Desc)}
            WepSkill: {self.WepSkill}: {type(self.WepSkill)}
            WepStrength: {self.WepStrength}: {type(self.WepStrength)}
            WepAP: {self.WepAP}: {type(self.WepAP)}
            WepDamage: {self.WepDamage}: {type(self.WepDamage)}
            WepAttacks: {self.WepAttacks}: {type(self.WepAttacks)}
            WepKeyWord: {self.WepKeyword}: {type(self.WepKeyword)}"""
      
class Target:
    def __init__(self,
                 TrgName, 
                 TrgDesc, 
                 TrgToughness, 
                 TrgWounds, 
                 TrgSave, 
                 TrgInvul, 
                 TrgKeyWord=[]
                 ):
        
        self.Name = TrgName
        self.Desc = TrgDesc
        self.TrgToughness = TrgToughness
        self.TrgWounds = TrgWounds
        self.TrgSave = TrgSave
        self.TrgInvul = TrgInvul
        self.TrgKeyWord = TrgKeyWord

    def __str__(self):
        return f""""TrgName: {self.Name}: {type(self.Name)}
            TrgDesc: {self.Desc}: {type(self.Desc)}
            TrgToughness: {self.TrgToughness}: {type(self.TrgToughness)}
            TrgWounds: {self.TrgWounds}: {type(self.TrgWounds)}
            TrgSave: {self.TrgSave}: {type(self.TrgSave)}
            TrgInvul: {self.TrgInvul}: {type(self.TrgInvul)}
            TrgKeyWord: {self.TrgKeyWord}: {type(self.TrgKeyWord)}
        """



#load weapon file
#file should be stored and loaded as a json file.
#End goal file will read/write from UI
def WeaponLoader():
    with open("WH10thWeapon.json") as WeaponFile:
        WeaponDict = json.load(WeaponFile)
    WeaponObjectList = []
    for weapon in WeaponDict:
        WeaponObjectList.append(Weapon(WeaponDict[weapon].get("Name"),
                                       WeaponDict[weapon].get("Description"),
                                       WeaponDict[weapon].get("BSSkill"),
                                       WeaponDict[weapon].get("Strength"),
                                       WeaponDict[weapon].get("AP"),
                                       WeaponDict[weapon].get("Damage"),
                                       WepKeyWord=WeaponDict[weapon].get("KeyWord")))
    return WeaponObjectList  
  
def WeaponDisplay(DisplayList):
    with dpg.table(header_row=True, row_background=True, borders_outerH=True, tag="WeaponParent", parent= "RollParent")as WeaponTableID:
        dpg.add_table_column(label="Unit")
        dpg.add_table_column(label="Description")
        dpg.add_table_column(label="Weapon Skill", tag= "WepSkill")
        with dpg.tooltip("WepSkill"):
            dpg.add_text("Balistic/Weapon skill of the unit using profile")
        dpg.add_table_column(label="Weapon Strength")
        dpg.add_table_column(label="AP")
        dpg.add_table_column(label="Damage")
        dpg.add_table_column(label="Attacks")
        dpg.add_table_column(label="Keywords")

        for weapon in DisplayList:
            with dpg.table_row():
                dpg.add_text(weapon.Name)
                dpg.add_text(weapon.Desc)
                dpg.add_text(weapon.WepSkill)
                dpg.add_text(weapon.WepStrength)
                dpg.add_text(weapon.WepAP)
                dpg.add_text(weapon.WepDamage)
                dpg.add_text(weapon.WepAttacks)
                dpg.add_listbox(weapon.WepKeyword, width= 300)

    return WeaponTableID

#load weapon file
#file should be stored and loaded as a json file.
#End goal file will read/write from UI
def TargetLoader():
    with open("WH10thTarget.json") as TargetFile:
        TargetDict = json.load(TargetFile)
    TargetObjectList = []
    for target in TargetDict:
        TargetObjectList.append(Target(TargetDict[target].get("Name"),
                                       TargetDict[target].get("Description"),
                                       TargetDict[target].get("Toughness"),
                                       TargetDict[target].get("Wounds"),
                                       TargetDict[target].get("Save"),
                                       TargetDict[target].get("Invul"),
                                       TargetDict[target].get("KeyWord")))
    return TargetObjectList

def TargetDisplay(DisplayList):
    with dpg.table(header_row=True, row_background=True, borders_outerH=True, tag="TargetParent", parent="RollParent"):
        dpg.add_table_column(label="Unit")
        dpg.add_table_column(label="Decription")
        dpg.add_table_column(label="Toughness")
        dpg.add_table_column(label="Wounds")
        dpg.add_table_column(label="Save")
        dpg.add_table_column(label="Invul save")
        dpg.add_table_column(label="Keywords")

        for target in DisplayList:
            with dpg.table_row():
                dpg.add_text(target.Name)
                dpg.add_text(target.Desc)
                dpg.add_text(target.TrgToughness)
                dpg.add_text(target.TrgWounds)
                dpg.add_text(target.TrgSave)
                dpg.add_text(target.TrgInvul)
                dpg.add_listbox(target.TrgKeyWord, width=100)

    return
def AddNewWeapon():
    pass

def AddNewTarget():
    pass

