



import cv2
import numpy as np

img = cv2.imread('Data_Bottles.png')


img = cv2.copyMakeBorder(img, 15, 15, 15, 15, cv2.BORDER_CONSTANT, value=[255, 255, 255])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.GaussianBlur(gray, (7, 7), 1)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 20      
params.maxThreshold = 220         

 
params.filterByArea = True
params.minArea = 240     
params.maxArea = 10000                   


params.filterByCircularity = True
params.minCircularity = 0.20  
params.filterByConvexity = True
params.minConvexity = 0.50   
params.filterByInertia = True
params.minInertiaRatio = 0.20   

params.minDistBetweenBlobs = 15   
params.blobColor = 0

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(gray_blur)

print(f"Bottles detected: {len(keypoints)}")

result = cv2.drawKeypoints(img, keypoints, np.array([]), (0,255,0),
                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



cv2.imwrite('result_tuned.png', result)

