import numpy as np 
from scipy.misc import imread,imresize
import matplotlib.pyplot as plt 

img=imread('youtubekm.jpg')
img_tinted=img*[1,0.95,0.1]

#show original image
plt.subplot(1,2,1)
plt.imshow(img)

#show tinted image
plt.subplot(1,2,2)
plt.imshow(np.uint8(img_tinted))
plt.show()