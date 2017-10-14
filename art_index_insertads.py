 #http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import shutil 
# Set the directory you want to start from

#print('first check')


#def replaceX():
#	pass

def flist(bakName):
  #t="dir,name,twi,extra\n"
  t=""
  for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
     
    for fname in fileList:
        #print('\t%s' % fname)
        if fname =="index.html":
            t=dirName+'\\'+fname
            tBak = dirName+'\\'+bakName
            shutil.copyfile(t,tBak)
            print (tBak)
            #replaceX()
  return t

# writing csv
rootDir = '.\\_build'
fName = ".\\_build\\index.html"
fo = open(fName,'r')
fstr = fo.read()
num = fstr.count('menu-img thumbnail')
print (num)
#ft = flist(bakName) 
#print (ft) 
#with open('index-list.csv', 'w') as f:
#      f.write(ft)

 