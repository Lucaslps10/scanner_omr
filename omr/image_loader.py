# Carrega imagem (com exceção)


import cv2
from .exceptions import ImageNotFoundException

class ImageLoader:
    def __init__(self, filepath: str):
        self.__filepath = filepath
        self.__image = None

    def load(self):
        image = cv2.imread(self.__filepath)
        if image is None:
            raise ImageNotFoundException(f"Arquivo não encontrado ou inválido: {self.__filepath}")
        self.__image = image

    def get_image(self):
        return self.__image
