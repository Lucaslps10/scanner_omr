# Faz grayscale, blur e edge detection
import cv2

class ImagePreprocessor:
    def __init__(self, image):
        self._image = image
        self._gray = None
        self._blurred = None
        self._edged = None

    def process(self):
        self._gray = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        self._blurred = cv2.GaussianBlur(self._gray, (5, 5), 0)
        self._edged = cv2.Canny(self._blurred, 75, 200)

    def get_gray(self):
        return self._gray

    def get_blurred(self):
        return self._blurred

    def get_edged(self):
        return self._edged
