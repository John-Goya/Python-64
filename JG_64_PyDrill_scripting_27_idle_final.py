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

'''
destination = os.listdir(dir_src)

for file in destination:
    if mtime > ago:
     shutil.move(dir_src+file,dir_dst) 
     print(file)

#shutil.copyfile(fname)

-----------------------------------------------

dir_src = ('c:/Users/John/Desktop/folder1/')
dir_dst = ('c:/Users/John/Desktop/folder2/')
destination = os.listdir(dir_src)

for file in destination:
    if file.endswith(".txt"):
     shutil.move(dir_src+file,dir_dst) 
     print(file)
'''
'''
os.chdir('C:\\') #Make sure you add your source and destination path below

dir_src = ('c:/Users/John/Desktop/folder1/')
dir_dst = ('c:/Users/John/Desktop/folder2/')

for filename in os.listdir(dir_src):
    if filename.endswith('.txt'):
        shutil.copy( dir_src + filename, dir_dst)
    print(filename)


file_startpath = 'C:/Users/John/Desktop/folder1/'
file_movepath = 'C:/Users/John/Desktop/folder2/'
destination = os.listdir(file_startpath)

for file in destination:
    if file.endswith(".txt"):
     shutil.move(file_startpath+file,file_movepath) 
     print(file)




	
then use st=os.lstat(filepath) and the st.st_mtime field and check if the difference to the current time is less than 1800 -- thats it. – hochl Nov 10 11 at 23:24


import os
import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(minutes=30)

for root, dirs,files in os.walk('.'):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print('%s modified %s'%(path, mtime))

-----------------------------------
https://stackoverflow.com/questions/8087693/python-code-to-find-all-newly-created-modified-and-deleted-files-in-all-the-dir

import os,time
print('modified time: ' + time.ctime(os.path.getmtime('c:/Users/John/Desktop/folder2/')))
print('created time:' + time.ctime(os.path.getctime('c:/Users/John/Desktop/folder2/')))

'''





'''
import os
import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(minutes=30)

for root, dirs, files in os.walk('.'):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print('%s modified %s'%(path, mtime))
--------------------------------
'''
'''
import os
import time
st = os.stat("c:/Users/John/Desktop/folder2/text1.txt")
ctime = st.st_ctime
print time.time() - ctime/3600 // hours
if mtime<24:
       print mtime

----------------------------------
'''
'''
import shutil
import os
import platform

find c:/Users/John/Desktop/folder2/ -mmin -61
----------------------------------
'''
'''
import os
import platform

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
'''
