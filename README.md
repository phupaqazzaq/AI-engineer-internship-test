# AI-engineer-internship-test
For Internship application at Connect Tech company

-- Description--
This program detects and counts bottle caps in an image using OpenCV's
SimpleBlobDetector. It outputs an draw the image with green circles drawn
around each detected cap and a total count displayed on screen.

-- Idea -- 
I noticed that the image given have main distinction which is the bottle cap which have darker color.
The main challenge is the plastic wrap that reflects light and the gap between bottles that a black shadow causing hallucinations.
I use blob detection from cv2 library to detect a circular object, which is the bottle cap.
I use gaussian blur to negates the plastic wraps shrinks that reflects light that may cause the blob detection to malfunction
# parameters
min,max threshhold = setting threshold separating bottle caps from background
min,max area = setting the range of possible bottle cap area
min circularity = setting this to filter out the false positive of the wrinkles
min convexity = setting this to filter out the irregular shadow that is not convex(เว้า) enough to be the caps
min inertia = setting this to filter out the irregular shadow that is too elongated to be the caps
minDistBetweenBlob = min distance between blobs to filter out hallucination that may cause by the shadows between the bottle's gap

-- Requirement --
Python 3.7 or higher is required. Install the dependencies using pip:
    -- put this in terminal --
    pip install opencv-python numpy


-- how to put imgae in program --

1. Place your input image in the same folder as the script.

2. Open the script and ensure the filename on this line matches your image/path

    Example img = cv2.imread('Data_Bottles.png')

   Replace 'Data_Bottles.png' with your actual image filename/path if different.

3. Run and debug the script


-- Output --
The preferable output in terminal is 
    "Bottles detected: 130"

The Image showing result of blob detecting is "result_tuned.png" 
 
# Disclaimer
    I try to tuned the program to count all bottles but it miss 1 bottle (the fourth bottle from the right following x-axis)
