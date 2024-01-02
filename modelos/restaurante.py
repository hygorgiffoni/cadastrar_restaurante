'''Módulo para classe de cadastrar novos restaurantes'''

from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas características.'''
    restaurantes = []
    def __init__(self, nome, categoria):
        '''
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        '''
        self.nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        '''Lista os restaurantes cadastrados'''
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')
        for rest in cls.restaurantes:
            print(f'{rest.nome.ljust(25)} | {rest.categoria.ljust(25)} | {str(rest.media_avaliacoes).ljust(25)} |{rest.ativo}')

    @property
    def ativo(self):
        '''Altera a descrição do atributo ativo do restaurante'''
        return 'Ativo' if self._ativo else 'Inativo'

    def alternar_status(self):
        '''Alterna o status do restaurante'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Recebe a nota atribuida ao restaurante'''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula a média das notas do restaurate'''
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media
