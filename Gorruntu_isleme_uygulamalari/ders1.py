import cv2
import numpy as np
from matplotlib import pyplot as plt

araba=r"C:\Users\sms\Desktop\car.jpg"
trafic=r"C:\Users\sms\Desktop\trafic_deneme.png"

# Görselleri yükleyin
template = cv2.imread(araba, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(trafic, cv2.IMREAD_GRAYSCALE)

# Şablon boyutunu alın
w, h = template.shape[::-1]

# Şablon eşleme metodunu uygulayın
res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Eşik değeri belirleyin
threshold = 0.1
loc = np.where(res >= threshold)

# Şablona uyan alanları çerçeve içine alın
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Sonucu göster
plt.imshow(image, cmap='gray')
plt.title('Tespit Sonucu'), plt.xticks([]), plt.yticks([])
plt.show()
