# Open-Webcam--using-OpenCV
OpenCV provides a video capture object which handles everything related to opening and closing of the webcam. 

first, we Import libraries OpenCV.
Then we use VideoCapture(0) function to capture the feed of the webcam - here 0 indicates the default value of webcam.
Now read the frame of the camera frame by frame - here ret is a boolean variable that checks if the camera is on or not
the frame is a variable in which all the camera feed is being saved
4. Here we close the loop and destroy all the windows and release the camera feed.
