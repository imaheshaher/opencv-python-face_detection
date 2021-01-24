import cv2
import sys
import os
import shutil

src_folder = os.getcwd()
print(src_folder)
# imagePath =  src_folder  + str(img_folder)
imagePath = "D:\Python\wpnotfaceimage" #Give Here directory path which images are scan

new_img_path="D:\Python\wpnotfaceimage" #those images which face is not detect
not_face_path = "D:\Python\wpfaceimage" #those images which face is detect
imglist = os.listdir(imagePath)
cnt =1
# print(imglist)
for i in imglist:
    imgname=os.path.join(imagePath,i)
    isFile = os.path.isfile(imgname)
    if not isFile:
        break
    else:
        image = cv2.imread(imgname)
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
        )
        iname=os.path.splitext(i)[0]
        img_name = '\\{}.jpg'.format(iname)

        if len(faces) == 0:
            change_path = not_face_path + str(img_name)
            try:
                shutil.copyfile(imgname,change_path)
            except:
                pass
            
            print("Not found face")
        else:
            print("[INFO] Found {0} Faces!".format(len(faces)))

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cnt+=1
            change_path = new_img_path + str(img_name)
            print(change_path)
            shutil.copyfile(imgname,change_path)
            #status = cv2.imwrite(change_path, image)   
            print("[INFO] Image faces_detected.jpg written to filesystem: ")