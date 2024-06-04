import cv2

import os
cap = cv2.VideoCapture("Move-20240602T124829Z-001/Move/_import_62bbfe2ad003e6.91946561_720p_5000br.mp4")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
lm_list = []
if frame_count > 30:
    frame_count_each = frame_count // 25  
    for y in range(frame_count_each):
        for i in range(25):
            ret, frame = cap.read()
            if ret:
                cv2.imshow("image", frame)
                if cv2.waitKey(1) == ord('q'):
                    break
                print("finish" + str(y))
        cap.release()
        cv2.destroyAllWindows()