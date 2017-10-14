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
count = 99999
sourceIndex = "list-thumb-01.csv"
fl = open(sourceIndex,'r')
for thumbF in fl:
    i = i +1
    if i < count:
        thumbF = thumbF.replace('\n','')
        nameArr = thumbF.split('\\')
        #objName = 'images/'+nameArr[2]+'/'+nameArr[3]
        objName = thumbF.replace('.\\_build','images')
        objName = objName.replace('\\','/')
        data = open(thumbF, 'rb')
        s3.Bucket('artlisa.org').put_object(Key=objName, Body=data)
        #print (objName)
        print (objName)
    #break