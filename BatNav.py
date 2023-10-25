#!/usr/bin/env python
# -*- coding: utf-8 -*-

Aircraft_carrier ={(2,2):False,(2,3):False,(2,4):False,(2,5):False,(2,6):False}
Carrier = {(4,1):True,(5,1):True,(6,1):True,(7,1):True}
Destroyer = {(5,3):True,(6,3):True,(7,3):True}
Submarine = {(5,8):True,(5,9):True,(5,10):True}
Torpedo_boat={(9,1):True,(9,2):True}

while Aircraft_carrier:
    print("Donnez les coordonées de votre tir")
    ligne= int (input("Donnez le numero de ligne"))
    colonne = int (input("Donnez le numero de colonne"))
    coord =(ligne,colonne)
    touches = 0
    if coord in Aircraft_carrier:print("Aircraft_carrier touché")
    Aircraft_carrier[coord]= False
for HitPoint in Aircraft_carrier.values():
    # print(HitPoint)
    if (HitPoint == False):
        touches +=1
if (touches == len(Aircraft_carrier)):
    print("Aircraft_carrier sunk!")
