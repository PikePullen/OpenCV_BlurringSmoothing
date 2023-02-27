import numpy as np
import matplotlib.pyplot as plt
import cv2

def load_image():
    img = cv2.imread('../DATA/bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()

# i = load_image()
# display_img(i)

# smaller the gamma, the closer to white
# gamma = 1/4
# result = np.power(i, gamma)
# display_img(result)

# the gamma over 1, the closer to black
# gamma2 = 8
# result2 = np.power(i, gamma2)
# display_img(result2)

"""Low pass filter with a 2d convolution"""
# img = load_image()
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(img, text='bricks', org=(10,600), fontFace=font, fontScale=10, color=(255,0,0), thickness=4)
# display_img(img)
#
# # 5x5 array of 1's make everything divided by 25... (1/25)=.04
# kernel = np.ones(shape=(5,5), dtype=np.float32)/25
# print(kernel)
#
# # this is blurred
# # image,desired depth
# dst = cv2.filter2D(img, -1, kernel)
# display_img(dst)

"""Blurred images 1"""
# img = load_image()
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(img, text='bricks', org=(10,600), fontFace=font, fontScale=10, color=(255,0,0), thickness=4)

# using cv2s built in blur kernel
# blurred = cv2.blur(img,ksize=(10,10))
# display_img(blurred)

"""Blurred images 2 - GaussianBlur"""
# img = load_image()
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(img, text='bricks', org=(10,600), fontFace=font, fontScale=10, color=(255,0,0), thickness=4)
#
# blurredImage = cv2.GaussianBlur(img, (5,5), 10)
# display_img(blurredImage)

"""Blurred images 2 - MedianBlur"""
# img = load_image()
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(img, text='bricks', org=(10,600), fontFace=font, fontScale=10, color=(255,0,0), thickness=4)
#
# blurredMedian = cv2.medianBlur(img, 5)
# display_img(blurredMedian)

"""Blurred images 3 - MedianBlur"""
# cleanImage = cv2.imread('../DATA/sammy.jpg')
# cleanImage = cv2.cvtColor(cleanImage, cv2.COLOR_BGR2RGB)
# display_img(cleanImage)
#
# noisyImage = cv2.imread('../DATA/sammy_noise.jpg')
# display_img(noisyImage)

# noise is pretty well cleared of noise, at the cost of detail
# median = cv2.medianBlur(noisyImage, 5)
# display_img(median)

"""Blurred images 4 - bilateral"""
# bilateral = load_image()
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(bilateral, text='bricks', org=(10,600), fontFace=font, fontScale=10, color=(255,0,0), thickness=4)
# bilateral = cv2.bilateralFilter(bilateral, 9, 75, 75)
# display_img(bilateral)