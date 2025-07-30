# Classe base de exceção personalizada;
# Herda da exceção padrão do Python (Exception), então pode ser usada para capturar erros específicos relacionados ao scanner.

class OMRException(Exception):
    """Exceção base para erros no scanner OMR."""
    pass

class ImageNotFoundException(OMRException):
    pass

class DocumentNotFoundException(OMRException):
    pass
