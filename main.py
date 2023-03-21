import Funcoes1, Funcoes2, FuncoesVini

while True:
    try:
        while True:
            try:
                valor1 = float(input('Digite o primeiro valor: '))
                break
            except ValueError:
                print('Digite apenas numeros!')
        while True:
            try:
                valor2 = float(input('Digite o segundo valor: '))
                break
            except ValueError:
                print('Digite apenas numeros!')

        while True:
            try:
                op = int(input('Qual operação você deseja?\n 1. Somar\n 2. Subtrair\n 3. Multiplicar\n 4. Dividir\n> 5. Hipotenusa\n> '))
                break
            except ValueError:
                print('Digite apenas numeros!')

        if op == 1:
            print('Resultado:',Funcoes1.somar(valor1,valor2))
            break
        elif op == 2:
            print('Resultado:',Funcoes1.subtrair(valor1,valor2))
            break
        elif op == 3:
            print('Resultado:',Funcoes2.multiplicação(valor1,valor2))
            break
        elif op == 4:
            print('Resultado:',Funcoes2.divisao(valor1,valor2))
            break
        elif op == 5:
            print('Resultado: ',FuncoesVini.hipo(valor1,valor2))
            break

    except ZeroDivisionError:
        print('Impossivel dividir por zero!')
        break
    except KeyboardInterrupt:
        print('\nPrograma finalizado!')
        break

