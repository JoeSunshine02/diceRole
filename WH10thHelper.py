#contains classes for WH10th SubType
import json 


#weapon class
class Weapon:

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
        
        self.WepName = WepName
        self.WepDesc = WepDesc
        self.WepSkill = WepSkill
        self.WepStrength = WepStrength
        self.WepAP = WepAP
        self.WepDamage = WepDamage
        self.WepAttacks = WepAttacks
        self.WepKeyword = WepKeyWord

    #Str print out
    def __str__(self):
        return f"""WepName: {self.WepName}: {type(self.WepName)}
            WepDesc: {self.WepDesc}: {type(self.WepDesc)}
            WepSkill: {self.WepSkill}: {type(self.WepSkill)}
            WepStrength: {self.WepStrength}: {type(self.WepStrength)}
            WepAP: {self.WepAP}: {type(self.WepAP)}
            WepDamage: {self.WepDamage}: {type(self.WepDamage)}
            WepAttacks: {self.WepAttacks}: {type(self.WepAttacks)}
            WepKeyWord: {self.WepKeyword}: {type(self.WepKeyword)}"""

#Target class   
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
        
        self.TrgName = TrgName
        self.TrgDesc = TrgDesc
        self.TrgToughness = TrgToughness
        self.TrgWounds = TrgWounds
        self.TrgSave = TrgSave
        self.TrgInvul = TrgInvul
        self.TrgKeyWord = TrgKeyWord

    def __str__(self):
        return f""""TrgName: {self.TrgName}: {type(self.TrgName)}
            TrgDesc: {self.TrgDesc}: {type(self.TrgDesc)}
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
