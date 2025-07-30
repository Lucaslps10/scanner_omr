# (herda ContourFinder) — detecta o documento pela forma quadrada

import cv2
from .contour_finder import ContourFinder
from .exceptions import DocumentNotFoundException

class DocumentDetector(ContourFinder):
    def __init__(self, image):
        super().__init__(image)
        self.__doc_contour = None

    def detect_document(self):
        if not self._contours:
            self.find_contours()

        if len(self._contours) == 0:
            raise DocumentNotFoundException("Nenhum contorno encontrado para o documento.")

        cnts_sorted = sorted(self._contours, key=cv2.contourArea, reverse=True)
        for c in cnts_sorted:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                self.__doc_contour = approx
                return self.__doc_contour

        raise DocumentNotFoundException("Documento (contorno com 4 pontos) não encontrado.")

    def get_document_contour(self):
        return self.__doc_contour
