import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./data source/Image_Filter_Input.png")
# img = cv2.imread("./data source/Image_Filter_Input.png",0)   #直接读入灰度图像, 默认是BGR彩色空间
img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for i in range(2000):   # 添加点噪声
    temp_x = np.random.randint(0, img_1.shape[0])  # img.shape[0]、img.shape[1]、img.shape[2]分别表示取图像的
    temp_y = np.random.randint(0, img_1.shape[1])  # 垂直尺寸、水平尺寸、通道数
    img_1[temp_x][temp_y] = 255  # 等价于 img_1[temp_x, temp_y] = 255

blur_1 = cv2.GaussianBlur(img_1, (5,5), 0)
blur_2 = cv2.medianBlur(img_1, 5)

plt.subplot(1,3,1), plt.imshow(img_1, 'gray')  # 这里的imshow函数是plt中的，和cv2里面的imshow函数不一样，默认是RGB(A)彩色空间
plt.subplot(1,3,2), plt.imshow(blur_1, "gray")
plt.subplot(1,3,3), plt.imshow(blur_2, "gray")
plt.show()

