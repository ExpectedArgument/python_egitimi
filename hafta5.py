# OPENCV uygulamaları
import cv2
import numpy as np
import matplotlib.pyplot as plt

# histogram ----------------

#img = cv2.imread("night.jpg")

# bluehistcv2 = cv2.calcHist([imgcv2],[0],None,[256],[0,255])
# greenhistcv2 = cv2.calcHist([imgcv2],[1],None,[256],[0,255])
# redhistcv2 = cv2.calcHist([imgcv2],[2],None,[256],[0,255])

# plt.plot(bluehistcv2, color = 'b')
# plt.plot(greenhistcv2, color = 'g')
# plt.plot(redhistcv2, color = 'r')


# imgcv2_contrasted = cv2.convertScaleAbs(imgcv2, alpha = 1.5, beta = 0)

# bluehistcv2 = cv2.calcHist([imgcv2_contrasted],[0],None,[256],[0,255])
# greenhistcv2 = cv2.calcHist([imgcv2_contrasted],[1],None,[256],[0,255])
# redhistcv2 = cv2.calcHist([imgcv2_contrasted],[2],None,[256],[0,255])
# plt.plot(bluehistcv2, color = 'b')
# plt.plot(greenhistcv2, color = 'g')
# plt.plot(redhistcv2, color = 'r')
# plt.show()

# lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# l_channel, a, b = cv2.split(lab)

# # Applying CLAHE to L-channel
# # feel free to try different values for the limit and grid size:
# clahe = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(8,8))
# cl = clahe.apply(l_channel)

# # merge the CLAHE enhanced L-channel with the a and b channel
# limg = cv2.merge((cl,a,b))

# # Converting image from LAB Color model to BGR color spcae
# enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

# # Stacking the original image with the enhanced image
# result = np.hstack((img, enhanced_img))
# cv2.imshow('Result', result)
# cv2.waitKey(0)

# threshold -----------------

# img = cv2.imread("manzara.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_new = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
# gray_new = gray_new[1]
# cv2.imshow("image",gray_new)
# cv2.waitKey(0)

# canny -----------------
# img = cv2.imread("manzara.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_new = cv2.Canny(gray, 100, 250)
# cv2.imshow("image",gray_new)
# cv2.waitKey(0)



# find contours -------------

# img = cv2.imread("circles.jpg")
# beyaz = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
# beyaz += 254
# cv2.imshow("image",beyaz)
# cv2.waitKey(0)


# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 220, 255, 0)
# cv2.imshow("thresholdd",thresh)
# cv2.waitKey(0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     cv2.drawContours(beyaz, contour, -1, (0,255,0), 3)
#     cv2.imshow("image",beyaz)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# find circles -------------
# img = cv2.imread("circles.jpg")
# beyaz = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
# beyaz += 254
# img = cv2.imread("circles.jpg")
# cv2.imshow("original",img)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray, 5)
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# circles = np.uint16(np.around(circles))
# print(circles)
# for i in circles[0,:]:
#     # draw the outer circle
#     cv2.circle(beyaz,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(beyaz,(i[0],i[1]),2,(0,0,255),3)
# cv2.imshow("circles",beyaz)
# cv2.waitKey(0)

# find lines ----------------
# img = cv2.imread("rect.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
# cv2.imshow("original",img)
# gray = cv2.medianBlur(gray, 5)
# edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# cv2.imshow("edges",edges)
# cv2.waitKey(0)


# VIDEO --------------
# cap = cv2.VideoCapture("output_10.avi")
# video_fps = cap.get(cv2.CAP_PROP_FPS)
# video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print("Video length: ", video_length)
# print("Video FPS: ", video_fps)
# print("Video width: ", video_width)
# print("Video height: ", video_height)
# print("Video duration(s): ", video_length/video_fps)
# frames = []
# c = 0
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         #cv2.imshow("frame", frame)
#         c+=1
#         print(c,end="\r")
#         if c == 500:
#             break
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         #frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
#         frames.append(frame)
#         # if cv2.waitKey(1) & 0xFF == ord('q'):
#         #     break
#     else:
#         break
# print(len(frames),video_length)
# cap.release()
# cv2.destroyAllWindows()
# # write video
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output_40.avi', fourcc, 40, (int(video_width), int(video_height)))
# frames_40 = []
# for i in range(len(frames)-1):
#     # if i%3 == 0:
#     #     frames_10.append(frames[i])
#     new_frame2 = cv2.addWeighted(frames[i], 0.5, frames[i+1], 0.5, 0.0)
#     new_frame1 = cv2.addWeighted(frames[i], 0.5, new_frame2, 0.5, 0.0)
#     new_frame3 = cv2.addWeighted(new_frame2, 0.5, frames[i+1], 0.5, 0.0)
#     frames_40.append(frames[i])
#     frames_40.append(new_frame1)
#     frames_40.append(new_frame2)
#     frames_40.append(new_frame3)

#     #new_frame = (frames[i] + frames[i+1])/2.
#     #new_frame = cv2.addWeighted(frames[i], 0.5, frames[i+1], 0.5, 0.0)
#     #frames_10.append(new_frame)
# for i in range(len(frames_40)):
#     frame = cv2.cvtColor(frames_40[i].astype(np.uint8), cv2.COLOR_GRAY2BGR)
#     out.write(frame)


# # get 5. second frame ----------------
# cap = cv2.VideoCapture("now_you_see_me.mp4")
# video_fps = cap.get(cv2.CAP_PROP_FPS)
# video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# sn = 5
# c = 0
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         #cv2.imshow("frame", frame)
#         c+=1
#         print(c,end="\r")
#         if c == sn*video_fps:
#             cv2.imshow("5. saniyedeki frame", frame)
#             cv2.waitKey(0)
#         # if cv2.waitKey(1) & 0xFF == ord('q'):
#         #     break
#     else:
#         break

