#main file for running rolling configuration

#imports
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from helper import *

ReqConfig = LoadMasterConfig()
ReqConfig.MasterValidate()

