from Reach_Kinematics import Kinematics
import random
import time

RA_km = Kinematics(COMPORT="COM6")

while True:
    x = random.uniform(0, 0.3)
    y = random.uniform(0, 0.3)
    z = random.uniform(0, 0.3)
    co = [[x,y,z]]
    print(co)
    RA_km.CalculateandMove(coordinates=co)
    
    



