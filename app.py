'''Executa o aplicativo'''
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_status()

def main():
    '''Executa o aplicativo'''
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
