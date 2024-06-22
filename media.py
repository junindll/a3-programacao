try:
    nota_1 = int(input("Digite a primeira nota: "))
    nota_2 = int(input("Digite a segunda nota: "))
    nota_3 = int(input("Digite a terceira nota: "))
    media = (nota_1 + nota_2 + nota_3) / 3

    if media >= 7:
        print(f'Sua média é {media}. Você passou, parabéns!!')
    elif media <= 7:
        print(f'Sua média ficou abaixo de 7. Infelizmente, você não passou.')
except:
    print('Você não digitou um número, tente novamente.')