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
marker = '<div class="menu-img thumbnail">'
num = fstr.count(marker)
print (num)
i = 0
itemIndex = 0
for i in range(0,num):
  itemIndex = fstr.find(marker,itemIndex)
  i  = i + 1
  print (fstr[itemIndex:itemIndex+60])
  itemIndex = itemIndex + 20
  print (i,itemIndex)
   
 