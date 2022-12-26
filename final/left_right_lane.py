import cv2 
import numpy as np


def filter_hough_lanes(hough_lines):
    new_hough_lines = []
    lanes =[]
    hough_lines_copy = hough_lines
    for id1, hough_line in enumerate(hough_lines):
        for id2, hough_line_copy in enumerate(hough_lines_copy):
            if id1 != id2:
                x1_orta = int((hough_line[0][0] + hough_line[0][2]) / 2)
                x2_orta = int((hough_line_copy[0][0] + hough_line_copy[0][2]) / 2)
                y1_orta = int((hough_line[0][1] + hough_line[0][3]) / 2)
                y2_orta = int((hough_line_copy[0][1] + hough_line_copy[0][3]) / 2)
                if abs(x1_orta - x2_orta) < 10 or abs(y1_orta - y2_orta) < 15:
                    #hough_lines.remove(hough_line)
                    #hough_lines_copy.remove(hough_line_copy)
                    yeni_merkez = [int((x1_orta + x2_orta) / 2), int((y1_orta + y2_orta) / 2)]
                    yeni_başlangic_x = int((hough_line[0][0] + hough_line_copy[0][0]) / 2)
                    yeni_başlangic_y =int( (hough_line[0][1] + hough_line_copy[0][1]) / 2)
                    yeni_bitis_x = int((hough_line[0][2] + hough_line_copy[0][2]) / 2)
                    yeni_bitis_y = int((hough_line[0][3] + hough_line_copy[0][3]) / 2)
                    yeni_egim = (yeni_bitis_y - yeni_başlangic_y ) / (yeni_bitis_x - yeni_başlangic_x)
                    
                    new_hough_lines.append([[yeni_başlangic_x, yeni_başlangic_y, yeni_bitis_x, yeni_bitis_y]])
                    lanes.append([yeni_merkez,yeni_egim])
                    break
                if id2 == len(hough_lines_copy) - 1:
                    merkez_x = int((hough_line[0][0] + hough_line[0][2]) / 2)
                    merkez_y = int((hough_line[0][1] + hough_line[0][3]) / 2)
                    egim = (hough_line[0][3] - hough_line[0][1]) / (hough_line[0][2] - hough_line[0][0])

                    new_hough_lines.append([hough_line[0]])
                    lanes.append([[merkez_x, merkez_y],egim])  
    return lanes, new_hough_lines

def filter_lanes(lanes):
    #new_lanes = []
    lanes_copy = lanes
    for id1 , lane in enumerate(lanes):
        for id2, lane_copy in enumerate(lanes_copy):
            if id1 != id2:
                if ((lane[0][0]-lane_copy[0][0])**2 + (lane[0][1]-lane_copy[0][1])**2)**0.5 < 5:
                    lanes.remove(lane)
                    break
                # if id2 == len(lanes_copy) - 1:
                #     pass#new_lanes.append(lane)
    return lanes



class left_right_lane():
    def __init__(self):
        pass

    def draw_line(self,lane):
        merkez_x, merkez_y = lane[0]
        egim = lane[1]
        x_alt = merkez_x + int((self.img_h-merkez_y)/egim)
        y_alt = self.img_h
        y_ust = int(self.img_h*5.5/10)
        x_ust = merkez_x - int((merkez_y-(self.img_h*5.5/10))/egim)
        cv2.line(self.imgcv1, (x_alt, y_alt), (x_ust, y_ust), (255, 0, 0), 2)

    def do(self,img):
        self.imgcv1 = img
        self.img_h = self.imgcv1.shape[0]
        img_w = self.imgcv1.shape[1]

        imgcv1_gray = cv2.cvtColor(self.imgcv1, cv2.COLOR_BGR2GRAY)
        imgcv1_gray_blur = cv2.GaussianBlur(imgcv1_gray, (5,5), 0)
        # cv2.imshow("gray", imgcv1_gray)
        # cv2.waitKey(0)
        imgcv1_gray_blur_threshold = cv2.threshold(imgcv1_gray_blur, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # cv2.imshow("threshold", imgcv1_gray_blur_threshold)
        # cv2.waitKey(0)
        imgcv1_gray_blur_threshold_canny = cv2.Canny(imgcv1_gray_blur_threshold, 100, 200)
        # cv2.imshow("canny", imgcv1_gray_blur_threshold_canny)
        # cv2.waitKey(0)
        imgcv1_gray_blur_threshold_canny_dilation = cv2.dilate(imgcv1_gray_blur_threshold_canny, None, iterations=1)
        # cv2.imshow("dilation", imgcv1_gray_blur_threshold_canny_dilation)
        # cv2.waitKey(0)
        hough_lines = cv2.HoughLinesP(imgcv1_gray_blur_threshold_canny_dilation, 1, np.pi/180, 100, np.array([]), minLineLength=170, maxLineGap=15)

        c = 0
        while True:
            (lanes,hough_lines) = filter_hough_lanes (hough_lines)
            c += 1
            if c == 10:
                break
        while True:
            lanes = filter_lanes(lanes)
            c -= 1
            if c == 0:
                break
            
        for hough_line in hough_lines:
            x1, y1, x2, y2 = hough_line[0]
            #cv2.line(imgcv1, (x1, y1), (x2, y2), (0, 255, 0), 3)


        for lane in lanes:
            print(lane)
            #draw_line(lane)
            

        merkez_x = img_w/2. 

        min_sol_x_fark = 50000
        min_sag_x_fark = 50000
        for lane in lanes:
            x_fark = lane[0][0] - merkez_x
            if x_fark > 0:
                if x_fark < min_sol_x_fark:
                    min_sol_x_fark = x_fark
            if x_fark < 0:
                x_fark = -x_fark
                if x_fark < min_sag_x_fark:
                    min_sag_x_fark = x_fark

        for lane in lanes:
            x_fark = lane[0][0] - merkez_x
            if x_fark > 0:
                if x_fark == min_sol_x_fark:
                    x_sol = lane[0][0]
                    y_sol = lane[0][1]
                    egim_sol = lane[1]
            if x_fark < 0:
                if x_fark == - min_sag_x_fark:
                    x_sag = lane[0][0]
                    y_sag = lane[0][1]
                    egim_sag = lane[1]


        self.draw_line([[x_sol,y_sol],egim_sol])
        self.draw_line([[x_sag,y_sag],egim_sag])

        cv2.imshow("hough_lines", self.imgcv1)
        cv2.waitKey(33)