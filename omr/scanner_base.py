# ABC significa "Abstract Base Class".
# @abstractmethod obriga as classes filhas a implementarem esses métodos.

from abc import ABC, abstractmethod

class ScannerBase(ABC):
    """
    Classe base abstrata que define a interface padrão para todos os scanners.
    Todas as classes que herdarem de ScannerBase devem implementar esses métodos.
    """
    @abstractmethod
    def scan(self):
        """Executa o processo principal de análise"""
        pass

    @abstractmethod
    def get_result_image(self):
        """Retorna a imagem final com correção"""
        pass

    @abstractmethod
    def get_original_image(self):
        """Retorna a imagem original enviada"""
        pass
