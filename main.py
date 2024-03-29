import time

import cv2
import numpy as np
from face import FaceRecognition
retinaface = FaceRecognition()


# todo:视频路径
video_path      ="./qiandao.mp4"

capture = cv2.VideoCapture(video_path)

fps = 0.0
while(capture.isOpened()):
    t1 = time.time()
    # 读取某一帧
    ref, frame = capture.read()
    if not ref:
        break
    frame = retinaface.inference(frame)
            
    fps  = ( fps + (1./(time.time()-t1)) ) / 2
    print("fps= %.2f"%(fps))
    frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("video",frame)
    cv2.waitKey(1)
print("Video Detection Done!")


capture.release()
cv2.destroyAllWindows()

    
