def cadastrousuario():
    print('---=== Cadastro usuario ===---')
    cadastro = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    
    mensagem = f'Ola {cadastro}, você tem {idade} anos!'
    print(mensagem)

    while True:
        print('---=== Selecione um lazer ===---')
        print('== Opção 1 - Jogos   ==')
        print('== Opção 2 - Musicas ==')
        print('== Opção 3 - Filmes  ==')
        print('== Opção 4 - Youtube ==')
        print('== Opção 5 - Sair    ==')

        lazer = int(input('Digite o que gostaria de fazer: '))
        if lazer == 1:
            print('https://store.steampowered.com/?l=portuguese')
            input('Pressione Enter para continuar...')
        elif lazer == 2:
            print('https://open.spotify.com/intl-pt')
            input('Pressione Enter para continuar...')
        elif lazer== 3:
            print('https://www.netflix.com/browse')
            input('Pressione Enter para continuar...')
        elif lazer == 4:
            print('https://www.youtube.com/')
            input('Pressione Enter para continuar...')
        elif lazer == 5:
            break
        else:
            print('Digite uma opçao valida')
            input('Pressione Enter para continuar...')


            