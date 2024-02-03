somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = 0
totmulher20 = 0
for c in range(1, 5):
    print(('===== {}º PESSOA ====='.format(c)))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: '))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('A quantidade de mulheres menores de 20 anos é: {}.'.format(totmulher20))
