# Import libraries
import numpy as np
import cv2
import matplotlib as mp
import matplotlib.pyplot as plt


from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms



################################################################################
#	Main
################################################################################
def main():
    test_images = [
        '/home/artemis-ii/Documents/ComputerVision/HW3Q4/images/Blood-cells_12.Red-blood-ce.jpg',
        '/home/artemis-ii/Documents/ComputerVision/HW3Q4/images/neuron.jpg',
    ]
    '''Read images and convert to grayscale'''
    img2 = cv2.imread(test_images[0], cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread(test_images[1], cv2.IMREAD_GRAYSCALE)

    cv2.imshow("red blood cells",img1)
    cv2.imshow("neurons",img2)
    # cv2.waitKey(10000)

    img1 = cv2.equalizeHist(img1)
    binary = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    binary = cv2.bitwise_not(binary)

    kernel = np.ones((5,5), np.uint8)
    img_dilation = cv2.dilate(binary, kernel, iterations=3)
    img_erode = cv2.erode(img_dilation, kernel, iterations=2)
    cv2.imshow("dilation",img_erode)

    img_erode = cv2.bitwise_not(img_erode)


    cv2.imshow("binary",binary)
    ret, labels = cv2.connectedComponents(img_erode)

    print('objects number is:', ret-1)

    cv2.waitKey(10000)




if __name__ == "__main__":
    main() 