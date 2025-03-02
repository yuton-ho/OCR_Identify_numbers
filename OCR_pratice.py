import cv2
import matplotlib.pyplot as plt
import easyocr
from skimage import exposure
import numpy as np

# 讀取圖片
image = cv2.imread("PARKING LOT.png")  # 請將 "your_image.jpg" 替換為你的圖片路徑

# 檢查圖片是否成功載入
if image is None:
    print("無法讀取圖片，請檢查路徑！")
    exit()

# OpenCV 預設讀取為 BGR 格式，需轉換為 RGB 以正確顯示
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 顯示原始圖片


plt.figure(figsize=(6,6))  # 設定顯示大小
plt.imshow(image_rgb)
plt.axis("off")  # 隱藏座標軸
plt.title("Original Image")
plt.show()

# 設定裁剪區域 (y_start:y_end, x_start:x_end)
cropped_image = image[294:460, 443:700]  # 這裡是示範，你可以改變數值來選擇不同區域
# 顯示裁剪後的圖片
'''
plt.figure(figsize=(6,6))  # 設定顯示大小
plt.imshow(cropped_image)
plt.axis("off")  # 隱藏座標軸
plt.title("change Image")
plt.show()
'''
# 轉換到HSV顏色空間
hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
# 定義要保留的顏色範圍(這裡以紅色為例)
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])

# 創建遮掩的條件
mask = cv2.inRange(hsv, lower_red1, upper_red1)
# 創建結果
result = cropped_image.copy()

# 將紅色的區域變黑
result[mask > 0] = [0, 0, 0]

plt.figure(figsize=(6,6))  # 設定顯示大小
plt.imshow(result)
plt.axis("off")  # 隱藏座標軸
plt.title("cover Image")
plt.show()
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#設定OCR reader
def ocr_scan(image_path:str) -> str:
    
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(
            image_path,
            allowlist='0123456789', #設定可以辨識的字的範圍
            paragraph=False,
            min_size=10,
            text_threshold=0.5,
            link_threshold=0.4,
            low_text=0.4
        )
    recognize_text = " ".join(elem[1] for elem in result)


    return recognize_text

image_path = cropped_image
print(ocr_scan(image_path))
