import os
Projectpath=os.listdir('C:/Users/ThinkBook/Desktop/proje')
cssFolderCounter=0
jsFolderCounter=0
imagesFolderCounter=0
for folder in Projectpath:
    if folder=='CSS':
        cssFolderCounter=1
    if folder=='JS':
        jsFolderCounter=1
    if folder=='Images':
        imagesFolderCounter=1
if cssFolderCounter==0:
    os.mkdir(os.path.join('C:/Users/ThinkBook/Desktop/proje','CSS'))
if jsFolderCounter==0:
    os.mkdir(os.path.join('C:/Users/ThinkBook/Desktop/proje','JS'))
if imagesFolderCounter==0:
    os.mkdir(os.path.join('C:/Users/ThinkBook/Desktop/proje','Images'))
 
for file in Projectpath:
    if file.count('.css')>0:
        folderPath=os.path.join('C:/Users/ThinkBook/Desktop/proje','CSS')
        filePath=os.path.join(folderPath,file)
        open(filePath,'x')
        # os.remove(file)
    if file.count('.js')>0:
        folderPath=os.path.join('C:/Users/ThinkBook/Desktop/proje','JS')
        filePath=os.path.join(folderPath,file)
        open(filePath,'x')
        # os.remove(file)
    if file.count('.jpg')>0:
        folderPath=os.path.join('C:/Users/ThinkBook/Desktop/proje','Images')
        filePath=os.path.join(folderPath,file) 
        open(filePath,'x')
        # os.remove(file)
