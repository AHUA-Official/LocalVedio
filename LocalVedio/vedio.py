import cv2

# 本地摄像头索引（通常为0）
CAMERA_INDEX = 0

# 创建VideoCapture对象来访问摄像头
cap = cv2.VideoCapture(CAMERA_INDEX)

# 检查摄像头是否打开
if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

# 循环读取摄像头视频流并在窗口中显示
while True:
    # 从摄像头读取一帧视频
    ret, frame = cap.read()

    # 检查是否成功读取视频帧
    if not ret:
        print("Error: Failed to read frame from camera.")
        break

    # 在窗口中显示视频流
    cv2.imshow('Camera Feed', frame)

    # 检测按键，如果按下 'q' 键则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头对象并关闭窗口
cap.release()
cv2.destroyAllWindows()
