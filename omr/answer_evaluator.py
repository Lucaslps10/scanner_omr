# avalia respostas e calcula pontuação

import numpy as np
import cv2

class AnswerEvaluator:
    def __init__(self, question_contours, thresh_image, answer_key):
        self._question_contours = question_contours
        self._thresh = thresh_image
        self._answer_key = answer_key
        self._correct = 0

    def evaluate(self, paper_image):
        # iterar em blocos de 5 (5 opções por questão)
        for (q, i) in enumerate(range(0, len(self._question_contours), 5)):
            cnts = self._question_contours[i:i + 5]
            cnts = sorted(cnts, key=lambda c: cv2.boundingRect(c)[0])  # left to right

            bubbled = None
            for (j, c) in enumerate(cnts):
                mask = cv2.drawContours(
                    np.zeros(self._thresh.shape, dtype="uint8"), [c], -1, 255, -1)
                mask = cv2.bitwise_and(self._thresh, self._thresh, mask=mask)
                total = cv2.countNonZero(mask)
                if bubbled is None or total > bubbled[0]:
                    bubbled = (total, j)

            k = self._answer_key[q]
            color = (0, 0, 255)
            if k == bubbled[1]:
                color = (0, 255, 0)
                self._correct += 1
            cv2.drawContours(paper_image, [cnts[k]], -1, color, 3)

        score = (self._correct / len(self._answer_key)) * 100
        return score
