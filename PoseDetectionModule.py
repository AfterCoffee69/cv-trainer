import cv2
import mediapipe as mp
import math

class PoseDetector():
    def __init__(self, mode = False, upBody = False, modelComplexity = 1, 
                 smooth = True, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.upBody = upBody
        self.modelComplexity = modelComplexity
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose  = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.modelComplexity, self.smooth, 
                                     self.detectionCon, self.trackCon)
        
    def findPose(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            
        return img
            
    def findPosition(self, img, draw = True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                    
        return self.lmList
    
    def findAngle(self, img, p1, p2, p3, direction, draw=True,):
        # Получить лендмарки
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        
        # Подсчёт углов
        angle = math.degrees(
            math.atan2(y3 - y2, x3 - x2) -  math.atan2(y1 - y2, x1 - x2))

        if angle < 0:
            angle += 360

        if direction == "right":
            angle = 360 - angle
        # print(angle)
        
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 5)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 5)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 1)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 1)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 1)
            cv2.putText(img, str(int(angle)), (x2 + 15, y2 + 50), 
                       cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
            
        return angle