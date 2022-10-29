import cv2
# CAPTURING VIDEO FRAME
# Webcam...the 0 in the function allows webcam to be on
webcam = cv2.VideoCapture(0)
# you need a loop to read all the frames


# capture videos using openCV
cap = cv2.VideoCapture(0)
# checking if the camera is opened properly using the cap method for cameras
if (cap.isOpened() == False):
    print('webcam is not opened properly')

# setting the resolutions and then converting the values to integer values
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# video coded ... encoders and decoders( there are many of these in the market)
# encoders and decoders block unnecessary things from the video
video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output = cv2.VideoWriter('Captured_video', video_cod, 30, (frame_width, frame_height))

while (True):
    ret, frame = cap.read()
    if ret == True:
        video_output.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break
cap.release()
video_output.release()
cv2.destroyAllWindows()
print('saved successfully')

# COMPARE CODE FOR BASIC WEBCAM START UP ABOVE AND THAT FOR SAVING AND ENCODING AND DECODING
# playing the video on the code
cap = cv2.VideoCapture('Captured_video')
while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitkey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
