# Importa todas as funções dos arquivos
from Funcoes1 import *
from Funcoes2 import *
from FuncoesVini import *
from funcoesLuis import *

# Loop principal
while True:
    try:
        # Pega os dois valores usando a função return_float
        valor1 = return_float('Digite o primeiro valor: ')
        valor2 = return_float('Digite o segundo valor: ')
        # Pega um valor digitado pelo usúario usuando a função return_int
        match return_int('Qual operação você deseja?\n 1. Somar\n 2. Subtrair\n 3. Multiplicar\n 4. Dividir\n 5. Hipotenusa\n> '):
            # Caso o valor digitado seja 1
            case 1:
                print('Resultado:',somar(valor1,valor2))
            # Caso o valor digitado seja 2
            case 2:
                print('Resultado:',subtrair(valor1,valor2))
            # Caso o valor digitado seja 3
            case 3:
                print('Resultado:',multiplicação(valor1,valor2))
            # Caso o valor digitado seja 4
            case 4:
                print('Resultado:',divisao(valor1,valor2))
            # Caso o valor digitado seja 5
            case 5:
                print('resultado',hipo(valor1, valor2))
            # Caso o valor digitado não esteja na lista acima
            case _:
                print('Valor inválido!')

    # Reinicia o programa se receber um ZeroDivisionError
    except ZeroDivisionError:
        print('Impossivel dividir por zero!')

    # Finaliza o programa se receber um KeyboardInterrupt
    except KeyboardInterrupt:
        print('\nPrograma finalizado!')
        break