# detecta bolhas marcadas
import cv2
import imutils
from imutils import contours

class BubbleDetector:
    def __init__(self, thresh_image):
        self._thresh = thresh_image
        self._question_contours = []

    def detect_bubbles(self):
        cnts = cv2.findContours(self._thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        questionCnts = []
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
            if w >= 20 and h >= 20 and 0.9 <= ar <= 1.1:
                questionCnts.append(c)
        self._question_contours = contours.sort_contours(questionCnts,
                                                        method="top-to-bottom")[0]
        return self._question_contours
