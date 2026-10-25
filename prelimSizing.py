# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:18:54 2026

@author: daire
"""

from rocketprops.rocket_prop import get_prop
from CoolProp.CoolProp import PropsSI

#inputs
f=3000 #newtons

#from CEA 
cf=1.3487
isp=2103 #m/s
ar=3 #area ratio
pc=20 #bar
cstar=1559.4 #m/s

#inputsfrom emprical data
lstar= #newtons



def chamber():
    
   at=f/(cf*pc)#throat area
   vc=lstar*at #chamber volume
   