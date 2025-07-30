# binariza imagem

import cv2

class Thresholding:
    def __init__(self, gray_image):
        self._gray = gray_image
        self._thresh = None

    def apply_threshold(self):
        self._thresh = cv2.threshold(self._gray, 0, 255,
                                     cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    def get_threshold(self):
        return self._thresh
