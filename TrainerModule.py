import cv2
import numpy as np
import time
import keyboard as kb
import threading
import pygame
from gtts import gTTS
import PoseDetectionModule as pdm

def speak_number(num):
    text = str(num)
    speech = gTTS(text=text, lang='ru')
    speech.save(f'audio/{num}.mp3')
    
    pygame.mixer.init()
    pygame.mixer.music.load(f'audio/{num}.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
         pygame.time.delay(100)


def AITrainer(image, x1, x2, x3, direction, startAngle, endAngle):
    capture = cv2.VideoCapture(0)

    pTime = 0
    cTime = 0

    detector = pdm.PoseDetector() 
    count = 0.5
    dir = 0
    

    while True:
        # Вебкамера
        ret, img = capture.read()
        img = cv2.resize(img, (1920, 1080))

        # Фото
        # img = cv2.imread(image)
        # img = cv2.resize(img, (1920, 1080))
        
        img = detector.findPose(img)
        lmList = detector.findPosition(img, False)

        # Вывод лендмарок
        # for lm in lmList:
        #     print(lm) 

        if len(lmList) != 0:
            
            angle = detector.findAngle(img, x1, x2, x3, direction)

            per = np.interp(angle, (startAngle, endAngle), (0, 100))
            bar = np.interp(angle, (startAngle, endAngle), (650, 100))
            

            print("Угол: ", angle)
            # print("Процент выполнения: ", per)
            
            # Подсчёт повторений
            color = (255, 0, 255)
            if per >= 95:
                color = (0, 0, 255)
                if dir == 0:
                    dir = 1
            if per <= 5:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0
            if count != 0 and int(count) == count:
                threading.Thread(target=speak_number, args=(round(count),)).start()
                count += 0.5
            
            # Шкала выполнения
            cv2.rectangle(img, (1800, 100), (1875, 950), color, 5)
            cv2.rectangle(img, (1800, int(bar)), (1875, 950), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (1800, 75), cv2.FONT_HERSHEY_PLAIN, 
                        4, color, 4)
            
            # Счётчик повторений
            # cv2.rectangle(img, (0, 1080), (250, 830), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (50, 1030), cv2.FONT_HERSHEY_PLAIN, 
                        15, (0, 255, 0), 25)
            
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                    3, (0, 0, 255), 3)
        
        cv2.imshow("AI Trainer", img)
        cv2.waitKey(2)

        # cv2.imshow('Test', img)
        # cv2.waitKey(2)
        
        if kb.is_pressed("space"):
            cv2.destroyWindow("AI Trainer")
            break

# AITrainer(23,25,27)