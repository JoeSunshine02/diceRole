#Helper functions for program 
import dearpygui.dearpygui as dpg
import WH10thHelper as Wh10
#Interprate config file for rolling function
class RequiredConfig:
    # validation rules for required config

    #Constructor
    def __init__(self,GameType, 
                 GameSubType, 
                 DefNumberOfDice, 
                 DefNumberOfSides, 
                 DefValSuccess
                ):
        
        self.GameType = GameType
        self.GameSubType = GameSubType
        try:
            self.DefNumberOfDice = int(DefNumberOfDice)
        except:
             raise TypeError("DefNumberOfDice nust be integer")
        try:
            self.DefNumberOfSides = int(DefNumberOfSides)
        except:
             raise TypeError("DefNumberOfSides nust be integer")
        try:
            self.DefValSuccess = int(DefValSuccess)
        except:
             raise TypeError("DefValSucess nust be integer")

    #call all validation functions
    def MasterValidate(self):
         self.ValidateConfigNone()
         self.ValidateGameType()
         self.ValidateGameSubType()
         self.ValidateDefNumberOfDice()
         self.ValidateDefNumberOfSides()
         self.ValidateDefValSucess()

    #validate Master config values are not none
    def ValidateConfigNone(self):
        ErrorFound = False
        ErrorMsg = ""
        if self.GameType is None:
             ErrorMsg = ErrorMsg + "GameType"
             ErrorFound = True
        if self.GameSubType is None:
             ErrorMsg = ErrorMsg + "GameSubType"
             ErrorFound = True
        if self.DefNumberOfDice is None:
             ErrorMsg = ErrorMsg + "DefNumberOfDice"
             ErrorFound = True
        if self.DefNumberOfSides is None:
             ErrorMsg = ErrorMsg + "DefNumberOfSides"
             ErrorFound = True
        if self.DefValSuccess is None:
             ErrorMsg = ErrorMsg + "DefValSuccess"
             ErrorFound = True

        if ErrorFound:
             raise Exception("Fields contain None values: "+ ErrorMsg)
    
    #validate GameType
    def ValidateGameType(self):
        ValidGameType = ('WarHammer10', 'HorusHeresy3')
        try:
            ValidGameType.index(self.GameType)
        except:
            raise Exception(f"{self.GameType} is not a supported GameType.\n Supported GameType: {ValidGameType}")
    
    #validate GameSubType    
    def ValidateGameSubType(self):
        ValidGameSubType = ('WH10th', 'HH3rd')
        try:
            ValidGameSubType.index(self.GameSubType)
        except:
            raise Exception(f"{self.GameSubType} is not a supported GameSubType.\n Supported GameType: {ValidGameSubType}")
    
    #validate defualt number of dice
    def ValidateDefNumberOfDice(self):
        if self.DefNumberOfDice <1:
             raise Exception("Number of dice cannot be less then 1")
        if self.DefNumberOfDice >500:
            raise Exception("Number of dice cannot be greater then 500")
        if self.DefNumberOfDice >150:
             print("WARNING: Number of dice is greater then 150, performace may suffer")

    #validate defualt dice sides
    def ValidateDefNumberOfSides(self):
         if self.DefNumberOfSides <2:
              raise Exception("Dice sides cannot be less then 2")
         if self.DefNumberOfSides > 100:
              raise Exception("Dice sides cannot be greater then 100")
         if(self.DefNumberOfSides > 6):
              print("Configured number of sides exceeds standard 6")
    
    #validate defualt Val Sucess
    def ValidateDefValSucess(self):
         #DefValSucess might be deprciated soon.
         pass

    def PrintConfig(self):
         print("Loaded Config")
         print(f"{self.GameType}")
         print(f"{self.GameSubType}")
         print(f"{self.DefNumberOfDice}")
         print(f"{self.DefNumberOfSides}")
         print(f"{self.DefValSuccess}\n")

# validate config format. Main use before loading config into Master Config Object
def ConfigValidater(ConfigRow):
    #validate config lines for formating
    if ConfigRow.find(":") == -1:
            raise Exception("Config option is not formated Correctly. Options must end in a colon :")
    if ConfigRow.find("[") == -1 or ConfigRow.find("]") == -1 :
            raise Exception("Config value is not formated Correctly. Values must be wrapped in brackets [] :")
#load master config file into Required Config Object
def LoadMasterConfig():
    #Load config file into context
    with open("Config.txt") as Config:
        List = Config.readlines()

#Load required config into Required hash map
    RequiredDict = {"GameType":None,
                    "GameSubType":None,
                    "DefNumberOfDice":None,
                    "DefNumberOfSides":None,
                    "DefValSuccess":None
                    }
    ReqVal = RequiredDict.keys()

    for val in List:
        ConfigValidater(val)
        ConfigOpt = val[:val.find(":")]
        ConfigVal = val[val.find("[")+1:val.find("]")]

        #Validate Required Config
        validReq = False
        for req in ReqVal:
            if ConfigOpt == req:
                validReq = True
                RequiredDict[req] = ConfigVal
                break
        if not validReq:
            raise Exception("Config option "+ConfigOpt+" is not a valid configuration option")
    #print(RequiredDict)

    #build Req config object
    return RequiredConfig(GameType=RequiredDict["GameType"],
                          GameSubType=RequiredDict["GameSubType"],
                          DefNumberOfDice= RequiredDict["DefNumberOfDice"],
                          DefNumberOfSides= RequiredDict["DefNumberOfSides"],
                          DefValSuccess= RequiredDict["DefValSuccess"])

#loads approprate weapon list from details in MasterConfigObj
def MasterLoader(MasterConfigObj,LoadType, DisplayOnLoad, ParentTag):
     match LoadType:
         case "Weapon":
               LoadList = MasterWeaponLoader(MasterConfigObj)
         case "Target":
               LoadList = MasterTargetLoader(MasterConfigObj)
         case _:
               raise Exception(f"Load type: {LoadType} could not be found")
     if DisplayOnLoad:
        #  MasterElementCleanUp(ParentTag)
          MasterElementDisplay(LoadList, LoadType,MasterConfigObj.GameType, False)
     return LoadList
# returns weapon list from provided game type
def MasterWeaponLoader(MasterConfigObj):
     gameType = MasterConfigObj.GameType
     match gameType:
          case "WarHammer10":
            return Wh10.WeaponLoader()   
          case _:
            raise Exception(f"GameType {gameType} does not have a loader function")
# returns target list from provided game type
def MasterTargetLoader(MasterConfigObj):
     gameType = MasterConfigObj.GameType
     match gameType:
          case "WarHammer10":
            return Wh10.TargetLoader()   
          case _:
            raise Exception(f"GameType {gameType} does not have a loader function")
          

#Adds elemets to UI from provided Element Object
def MasterElementDisplay(DisplayList,DisplayType, GameType, DispalyModeSimple = True ):
    #simple display mode to display name and desc
     if DispalyModeSimple:
          with dpg.child_window(width = 1200, height = 200,tag=DisplayType):
             dpg.add_text(f"{DisplayType} list:".upper())
             for load in DisplayList:
                 with dpg.group(horizontal=True):
                    dpg.add_text(load.Name)
                    dpg.add_text(load.Desc)
          return
     
     #non-simple mode needs to check display type
     match DisplayType:
         case "Weapon":
               DisplayTagList = MasterWeaponDisplay(DisplayList, GameType)
         case "Target":
               DisplayTagList = MasterTargetDisplay(DisplayList, GameType)
         case _:
               raise Exception(f"display type: {DisplayType} could not be found")
     return DisplayTagList     

def MasterWeaponDisplay(DisplayList, gameType):
     match gameType:
          case "WarHammer10":
            return Wh10.WeaponDisplay(DisplayList)   
          case _:
            raise Exception(f"GameType {gameType} does not have a Display function")


def MasterTargetDisplay(DisplayList, gameType):
      match gameType:
          case "WarHammer10":
            return Wh10.TargetDisplay(DisplayList)   
          case _:
            raise Exception(f"GameType {gameType} does not have a Display function")


#delets element from provided tag and all children
#function can be called as a callback
def MasterElementCleanUp(sender, app_data,ParentTag):
     dpg.delete_item(ParentTag)

# Master Element Display Wrapper for callback
def MasterDisplayCallback(sender, app_data, user_data ):
    MasterElementDisplay(user_data[0],
                         user_data[1],
                         user_data[2],
                         user_data[3])
    
#clean call to end program.
def KillMain():
     dpg.destroy_context()



    
   