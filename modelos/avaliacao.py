'''Módulo para classe de avaliação dos restaurantes'''
class Avaliacao:
    '''Atribui uma nota para o restaurante'''
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
