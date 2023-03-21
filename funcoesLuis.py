'''
    Essa função mostra o 'texto' e lê um input
    Se não for digitado um número irá mostrar o texto escrito em 'erro'
    Vai repetir o processo até que o usuário digite um número
'''

# Função que retorna um float digitado pelo usuário
def return_float(texto, erro='Digite apenas numeros!'):
    # Loop eterno
    while True:
        try:
            # Tenta retornar um float do texto digitado pelo usuario
            return float(input(texto))
        except KeyboardInterrupt:
            # Se o usuário finalizar o programa, irá retornar a exceção KeyboardInterrupt
            raise KeyboardInterrupt
        except:
            # mostra a mensagem de erro
            print(erro)

# Função que retorna um int digitado pelo usuário
def return_int(texto, erro='Digite apenas um numero inteiro!'):
    # Loop eterno
    while True:
        try:
            # Tenta retornar um int do texto digitado pelo usuario
            return int(input(texto))
        except KeyboardInterrupt:
            # Se o usuário finalizar o programa, irá retornar a exceção KeyboardInterrupt
            raise KeyboardInterrupt
        except:
            # mostra a mensagem de erro
            print(erro)