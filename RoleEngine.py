class RoleEngine():
     def __init__(self):
          self.RoleWeapon = None
          self.RoleTarget = None
          self.AttackNum = None
          self.ExtraWeaponKeywords = None
          self.ExtraTargetKeywords = None

     def __str__(self):
         return f""" Weapon to role: {self.RoleWeapon}: {type(self.RoleWeapon)}
               Target to role: {self.RoleTarget}: {type(self.RoleTarget)}
               Number of attacks to role: {self.AttackNum}: {type(self.AttackNum)}
               Keywords to apply to weapon: {self.ExtraWeaponKeywords}: {type(self.ExtraWeaponKeywords)}
               Keywords to apply to target: {self.ExtraTargetKeywords}: {type(self.ExtraTargetKeywords)}"""
