使用OCR辨識數字
利用cv2讀取所需檔案，透過

plt.figure(figsize=(6,6))  # 設定顯示大小
plt.imshow(image_rgb)  #圖片檔案的變數
plt.axis("off")  # 隱藏座標軸
plt.title("Original Image")  #圖片標題
plt.show()
檢查檔案(對圖片的任意加工都可以用此了解效果) 
使用matplotlib.pyplot是為了方便知道要對圖片切個的座標，如下圖所示:
![image](https://github.com/user-attachments/assets/bf62cc51-c3ca-4330-bc89-1dd83be2fd8f)


鼠標移動到圖片上，右下角會出現對應座標。知道要切割的圖片的四個角落座標後，便可藉由下列函式切割。
![image](https://github.com/user-attachments/assets/9fa04062-0a4c-4bcb-b722-63c2e79fcb04)


現在有切割好的圖片，就只需要辨識圖片了
![image](https://github.com/user-attachments/assets/71209db4-7c20-40f2-829f-378e43d543ab)


設定allowlist很重要，這決定辨識結果。如果只要辨識數字就設定數字，否則容易辨識錯誤。
![image](https://github.com/user-attachments/assets/ce09cb36-8b3a-4eeb-81e7-fe166205cab9)


        
