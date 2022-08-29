from left_right_lane import left_right_lane as _
import cv2

# imgcv2 = cv2.imread('lane1.png')
# l = _()
# l.do(imgcv2)
# cv2.imwrite('lane1_out.png', imgcv2)

# read video
l = _()
cap = cv2.VideoCapture('driving.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # process frame
        try:
            l.do(frame)
        except :
            pass
    else:
        break

