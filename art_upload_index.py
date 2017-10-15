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
count = 999
sourceIndex = "index-list-01.csv"
fl = open(sourceIndex,'r')
for indexF in fl:
    i = i +1
    if i < count:
        indexF = indexF.replace('\n','')
        nameArr = indexF.split('\\')
        objName = 'images/'+nameArr[2]+'/'+nameArr[3]
        data = open(indexF, 'rb')
        s3.Bucket('artlisa.org').put_object(Key=objName, Body=data, ContentType='text/html')
        print (objName)
    #break