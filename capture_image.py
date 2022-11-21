import os
import cv2
import time
import uuid

IMAGE_PATH='CollectedImages'

labels=['0','1','2','3','4','5','6','7','8','9']

number_of_images=25

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(2)
    for imgnum in range(number_of_images):
        ret,frame=cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(0.5)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()