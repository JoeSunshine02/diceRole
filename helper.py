#Helper functions for program 

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

def ConfigValidater(ConfigRow):
    #validate config lines for formating
    if ConfigRow.find(":") == -1:
            raise Exception("Config option is not formated Correctly. Options must end in a colon :")
    if ConfigRow.find("[") == -1 or ConfigRow.find("]") == -1 :
            raise Exception("Config value is not formated Correctly. Values must be wrapped in brackets [] :")
    

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
            
        



    
   