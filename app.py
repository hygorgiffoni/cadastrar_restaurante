'''Executa o aplicativo'''
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_status()
restaurante_praca.receber_avaliacao('Cliente 1', 5)
restaurante_praca.receber_avaliacao('Cliente 2', 4)
restaurante_praca.receber_avaliacao('Cliente 3', 2)

def main():
    '''Executa o aplicativo'''
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
