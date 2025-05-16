while True:
    comando = input('Como posso ajudá-lo hoje? ')
    if comando == 'sair':
        print('Até a próxima!!')
        break
    if comando.lower()[0:6] != 'jarvis':
        print('Você não me chamou pelo meu nome. És um impostor? xD')
        continue
    else:
        print(f'Estou ouvindo! Você disse: {comando}')
    