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
adsense = '<div class="menu-img thumbnail">' \
          +'<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>' \
          +' <ins class="adsbygoogle" ' \
          +' style="display:block; text-align:center;" ' \
          +' data-ad-layout="in-article" ' \
          +' data-ad-format="fluid" ' \
          +' data-ad-client="ca-pub-8980136446658337" ' \
          +' data-ad-slot="6697182900"></ins>' \
          +'<script>' \
          +' (adsbygoogle = window.adsbygoogle || []).push({});' \
          +'</script>' \
          +'</div>'

rootDir = '.\\_build'
fName = ".\\_build\\index.html"
fo = open(fName,'r')
fstr = fo.read()
marker = '<img src="'
org = '<img src="'
rep = '<img src="images/'
fstr = fstr.replace(org,rep)
org = '<a href="'
rep = '<a href="images/'
fstr = fstr.replace(org,rep)
num = fstr.count(marker)
print (num)
i = 0
itemIndex = 0
beginNum = 0
gap = 9
for i in range(0,num):
  itemIndex = fstr.find(marker,itemIndex)
  i  = i + 1
  if i == beginNum:
       fstrBefore = fstr[:itemIndex]
       fstrAfter = fstr[itemIndex:]
       fstr = fstrBefore+adsense+fstrAfter
  #print (fstr[itemIndex:itemIndex+60])
  itemIndex = itemIndex + 20
  print (i,itemIndex)

nn = '.\\_build\\i_01.html'
nf = open(nn,'w')
nf.write(fstr)
print (nn)
 