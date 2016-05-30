# -*- coding: cp1252 -*-
# Função penalti
#pushbuttonPenalti_f.m

def pushbuttonPenalti_f:
    gui = guidata(GuiSimRobot)
       l = [1,2]
       for i in l:
       #set_motor_f(s,id,80,0,80,0)
       t = i
 
    for i in l:
        #set_motor_f(s,id,0,0,0,0)
        K=i
    
    set(gui.pushbuttonStart,'Callback','robotLoop_f')

