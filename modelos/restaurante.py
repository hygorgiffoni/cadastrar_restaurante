'''Módulo para classe de cadastrar novos restaurantes'''
class Restaurante:
    '''Classe para cadastrar novos restaurantes'''
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        '''Lista os restaurantes cadastrados'''
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for rest in cls.restaurantes:
            print(f'{rest.nome.ljust(25)} | {rest.categoria.ljust(25)} | {rest.ativo}')

    @property
    def ativo(self):
        '''Altera a descrição do atributo ativo do restaurante'''
        return 'Ativo' if self._ativo else 'Inativo'

    def alternar_status(self):
        '''Alterna o status do restaurante'''
        self._ativo = not self._ativo
