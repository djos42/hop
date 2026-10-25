# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:18:54 2026

@author: daire
"""

from rocketprops.rocket_prop import get_prop
from CoolProp.CoolProp import PropsSI
import math

#inputs
f=3000 #newtons
pe=1 #bar

#from CEA 
cf=1.3487
isp=2103 #m/s
ar=3 #area ratio
pc=20 #bar
cstar=1559.4 #m/s
gamma=1.141

#inputsfrom empirical data
lstar=0.85 



def chamber():
    
   at=f/(cf*pc) #throat area
   dt=2*math.sqrt(at/math.pi)
   w=(pc*at)/cstar
   vc = lstar*at  #chamber volume
   me=math.sqrt((math.pow((gamma/(1-gamma))(pe/pc))-1)/((gamma-1)/2))
   er=(1/me)*(((2/(gamma+1))*(1+((gamma+1)/2)*(me**2)))**((gamma+1)/((2*gamma)-2))) #expansion ratio
   