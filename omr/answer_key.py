# representa a chave de respostas

class AnswerKey:
    def __init__(self, key_dict):
        self._key = key_dict

    def get_key(self):
        return self._key
