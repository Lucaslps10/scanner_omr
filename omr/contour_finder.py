# Busca contornos

import imutils
import cv2

class ContourFinder:
    def __init__(self, image):
        self._image = image
        self._contours = []

    def find_contours(self):
        cnts = cv2.findContours(self._image.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        self._contours = imutils.grab_contours(cnts)
        return self._contours
