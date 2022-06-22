# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:31:01 2022

@author: TH
"""

import psychopy
from psychopy import visual, core, event, gui, prefs, sound, monitors, clock
import pandas as pd
import numpy as np

word_list=pd.read_excel('C:/Users/TH/Desktop/WordsCollection.xlsx',header=None)[0]
response=[]
react_t=[]
target=[]

def win():
    win=psychopy.visual.Window(
        size=[700,700],
        units="pix",
        fullscr=False
    )
    return win

def begin():
    begin=psychopy.visual.TextStim(win,text="Press any key to begin!",color=[1,1,1],pos=(0,0),height=(100))
    begin.draw()
    win.flip()
    psychopy.event.waitKeys()
    win.flip()
    
def fixation():
    fix_h=visual.Rect(win,width=60,height=1,units='pix',
                      lineColor=[-1,-1,-1],
                      fillColor=[-1,-1,-1],
                      pos=(0,0))
    fix_v=visual.Rect(win,width=1,height=60,units='pix',
                      lineColor=[-1,-1,-1],
                      fillColor=[-1,-1,-1],
                      pos=(0,0))
    fix_h.draw()
    fix_v.draw()

def sti(word_list):
    wtd=word_list
    word=psychopy.visual.TextStim(win,text=wtd,color=[1,1,1],pos=(0,0),height=(100))
    word.draw()
    win.flip()
    return wtd

def react():
    key=event.waitKeys(maxWait=2,keyList=['space'],modifiers=True,timeStamped=clock,
                        clearEvents=True) 
    if key==None:
        res_key='/'
        res_time='/'
    else:
        res_key=key[0][0]
        res_time=key[0][1]
    win.flip()    
    return res_key,res_time




sid=input()
clock=psychopy.core.Clock()

win=win()
begin()
fixation()
win.flip()
core.wait(1)
win.flip()
for i in range(3):
    fixation()
    win.flip()
    core.wait(0.5)
    win.flip()
    tar=sti(word_list[i])
    rk,rt=react()
    target.append(tar)
    response.append(rk)
    react_t.append(rt)
    win.flip()

win.close()

data=pd.DataFrame({'sid':sid,
                   'target':target,                 
                    'response_key':response,
                    'rt':react_t
                    })

# spath='C:/Users/TH/Desktop/data/'    
# file_name= sid+'ldt-text'+'.csv'
# save_path=spath+file_name
# data.to_csv(save_path, sep=',',index=False)


    