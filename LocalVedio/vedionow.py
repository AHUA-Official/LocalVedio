import cv2
import time
import requests
from datetime import datetime

CAMERA_INDEX =0
VIDEO_CODEC = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4格式编码
CAPTURE_INTERVAL_MS = 50  # 捕获间隔，这里以毫秒计，根据需要调整帧率
VIDEO_FILENAME = "temp_video.mp4"  # 临时视频文件名
UPLOAD_ENDPOINT = "http://8.137.104.90:5000/upload_video"
# 获取当前日期和时间
now = datetime.now()

# 格式化时间字符串，确保小时、分钟和秒都有前导零
time_str = now.strftime("%Y%m%d_%H%M%S")  # 年月日_时分秒格式

VIDEO_FILENAME = f"{time_str}_1s_temp_video.mp4"  # 临时视频文件名
# 初始化摄像头
cap = cv2.VideoCapture(CAMERA_INDEX)
if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

# 视频编写器初始化
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(VIDEO_FILENAME, VIDEO_CODEC, 20, (frame_width, frame_height))  # 假设FPS为20

try:
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from camera.")
            break

        # 写入帧到视频文件
        out.write(frame)

        # 检查是否达到一定的录制时间或手动停止条件
        elapsed_time = time.time() - start_time
        if elapsed_time > 1 or cv2.waitKey(1) & 0xFF == ord('q'):  # 示例：录制5秒或按'q'键停止
            break

    # 释放资源
    cap.release()
    out.release()

    # 上传视频文件
    with open(VIDEO_FILENAME, 'rb') as video_file:
        files = {'file': (VIDEO_FILENAME, video_file, 'video/mp4')}
        response = requests.post(UPLOAD_ENDPOINT, files=files)

        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Failed to upload video. Server responded with status code {response.status_code}")

    # 可以在这里选择是否删除临时视频文件
    # os.remove(VIDEO_FILENAME)

finally:
    cv2.destroyAllWindows()