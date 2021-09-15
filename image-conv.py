# from PIL import Image
# import PIL
# import os
# import glob

# all_files = os.listdir('/home/udoka/Desktop/VA/VredeVirtualServices/media')

# allImages = [eachFile for eachFile in all_files if eachFile.endswith(('jpg','png'))]

# for x in allImages:
#     fileX = '/home/udoka/Desktop/VA/VredeVirtualServices/media/'+x
#     images = Image.open(fileX)
#     images = images.convert('RGB')
#     fileB = '/home/udoka/Desktop/VA/VredeVirtualServices/media/'+fileX[0:2]+'.webp'
#     images.save(fileB,'webp')
import request

def contact_details():
    if request.method == 'POST':
        userName = request.form['contactName']
        userMail = request.form['contactMail']
        content = request.form['contentMessage']
    return{
        Name: userName,
        Mail: userMail,
        Message: content
    }

contact_details()