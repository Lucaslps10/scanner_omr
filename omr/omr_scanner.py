# fachada que orquestra todo processo

from omr.image_loader import ImageLoader
from omr.image_preprocessor import ImagePreprocessor
from omr.document_detector import DocumentDetector
from omr.perspective_transformer import PerspectiveTransformer
from omr.thresholding import Thresholding
from omr.bubble_detector import BubbleDetector
from omr.answer_evaluator import AnswerEvaluator
from omr.answer_key import AnswerKey
from omr.exceptions import OMRException


class OMRScanner:
    def __init__(self, image_path, answer_key_dict):
        self._image_path = image_path
        self._answer_key = AnswerKey(answer_key_dict)
        self._score = 0

        # Atributos internos
        self._original_image = None
        self._processed_image = None
        self._doc_contour = None
        self._warped_image = None
        self._warped_gray = None
        self._thresh = None
        self._question_contours = None

    # === PROPERTIES ===

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        if not isinstance(value, str) or not value.endswith(('.jpg', '.png')):
            raise ValueError("Caminho da imagem inválido.")
        self._image_path = value

    @property
    def answer_key(self):
        return self._answer_key

    @answer_key.setter
    def answer_key(self, value):
        if not isinstance(value, dict):
            raise ValueError("O gabarito deve ser um dicionário.")
        self._answer_key = AnswerKey(value)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Nota inválida.")
        self._score = value

    # === MÉTODOS DE PROCESSAMENTO ===

    def scan(self):
        """Executa o processo completo de correção da folha."""
        try:
            loader = ImageLoader(self._image_path)
            loader.load()
            self._original_image = loader.get_image()

            preprocessor = ImagePreprocessor(self._original_image)
            preprocessor.process()

            detector = DocumentDetector(preprocessor.get_edged())
            detector.find_contours()
            self._doc_contour = detector.detect_document()

            transformer = PerspectiveTransformer(self._original_image, self._doc_contour)
            transformer.transform()
            self._warped_image = transformer.get_warped()

            transformer_gray = PerspectiveTransformer(preprocessor.get_gray(), self._doc_contour)
            transformer_gray.transform()
            self._warped_gray = transformer_gray.get_warped()

            thresholder = Thresholding(self._warped_gray)
            thresholder.apply_threshold()
            self._thresh = thresholder.get_threshold()

            bubble_detector = BubbleDetector(self._thresh)
            self._question_contours = bubble_detector.detect_bubbles()

            evaluator = AnswerEvaluator(self._question_contours, self._thresh, self._answer_key.get_key())
            self._score = evaluator.evaluate(self._warped_image)

        except OMRException as e:
            print(f"Erro no processamento OMR: {e}")
            raise
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise

    # === MÉTODOS AUXILIARES ===

    def get_result_image(self):
        return self._warped_image

    def get_original_image(self):
        return self._original_image
