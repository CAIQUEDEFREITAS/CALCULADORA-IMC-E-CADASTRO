import os
from cadastro import cadastrousuario
from calculadora import calculaimc

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        limpar_console()

        print("---==== O que você deseja fazer? ====--- ")
        print('== Opção 1 - Calcular IMC ==')
        print('== Opção 2 - Cadastrar usuário ==')
        print('== Opção 3 - Sair ==')

        opcao  = input('Digite uma opçao: ')

        if opcao == '1':
            limpar_console()
            resultado_imc = calculaimc()
            print('Resultado do IMC:', resultado_imc)
            input('Pressione Enter para continuar...')
        elif opcao == '2':
            limpar_console()
            cadastrousuario() 
            input('Pressione Enter para continuar...')
        elif opcao == '3':
            print('Saindo do programa. Até mais!')
            break  # Sai do loop e encerra o programa
        else:
            print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
            input('Pressione Enter para continuar...')


if __name__ == "__main__":
    main()

