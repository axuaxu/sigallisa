import boto3
import os
# Let's use Amazon S3
s3 = boto3.resource('s3')
##s3.Bucket('artlisa.org').put_object(Key='index-list.csv', Body=data)
bucket = s3.Bucket('artlisa.org')
print (bucket)
#for object in bucket.objects.all():
#    print(object)
#sourceDir = '.\\_build\\'
#destDir = 'images/emile-claus/'
 
i = 0
count = 3
 
rootDir = '.\_build'

def flist():
  #t="dir,name,twi,extra\n"
  t=""
  for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
     
        #print('\t%s' % fname)
    for thumb in subdirList:
        if thumb =="thumbnails":
            for fname in fileList:
                #dirN = dirName.replace('.\\_build\\','images/')
                t=t+dirName+'\\'+thumb+'\\'+fname+'\n'
                #print (t)
            #replaceX()
  return t


 
        #s3.Bucket('artlisa.org').put_object(Key=objName, Body=data)
        #print (objName)
    #break
tstr = flist()
listT = "list-thumb.csv"
listF = open(listT,"w")
listF.write(tstr)
print("output: %s" % listT)