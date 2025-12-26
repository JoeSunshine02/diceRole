#class contains keywords unique for warhammer 40k 10th edition
def lethalHits( intRoleValue, **Config):
    if(intRoleValue >= Config["ValSuccess"]):
        return True
    return False

def sustainedHits(intRoleValue, **Config):
    if(intRoleValue >= Config["ValSuccess"]):
        return 1+Config["ValSustained"]
    return 1

def DevWounds(intRoleValue, **Config):
    if(intRoleValue >= Config["ValSucess"]):
        return True
    return False
#def antiUnit(intRoleValue,strTargetType **Config):
 #   #assume target is a valid 
  #  if()  