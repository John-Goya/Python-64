# -*- coding: cp1252 -*-
#   64_PyDrill_Datetime_27_idle
#
#   John Goya
#
#   For Python Drill #64 - Daily File Transfer scripting project - Python 2.x - IDLE.
#

import os
import time
import shutil
import datetime

now = datetime.datetime.now()
ago = now-datetime.timedelta(hours=24)
dir_src = 'c:/Users/John/Desktop/folder1/'
dir_dst = 'c:/Users/John/Desktop/folder2/'

for root,dirs,files in os.walk(dir_src):
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = datetime.datetime.fromtimestamp(st.st_mtime)        
        if mtime > ago:
            print 'Filename:', fname, '\n Time created/modified :',mtime.strftime("%H:%M %m/%d/%Y \n")
            shutil.copy(path, dir_dst)
