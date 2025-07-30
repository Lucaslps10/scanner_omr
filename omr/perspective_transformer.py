# aplica transformação perspectiva
from imutils.perspective import four_point_transform

class PerspectiveTransformer:
    def __init__(self, image, contour):
        self._image = image
        self._contour = contour
        self._warped = None

    def transform(self):
        self._warped = four_point_transform(self._image, self._contour.reshape(4, 2))

    def get_warped(self):
        return self._warped
