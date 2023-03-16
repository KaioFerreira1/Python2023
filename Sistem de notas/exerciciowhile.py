#lista das notas
notas = []

#O while ler as notas e verifica se tem as respectivas tres notas
while len(notas) < 3:
    nota = float(input('Digite a nota da prova {}: '.format(len(notas) + 1)))
    #Caso o usuario digite notas invalidas ou seja menor que 0 ou maior que 10 gera um "erro".
    if nota < 0 or nota > 10:
        print('Nota inválida. Digite um valor entre 0 e 10.')
    else:
        notas.append(nota)

media = sum(notas) / len(notas)

if media >= 6:
    print('Parabéns, você foi aprovado com média {:.2f}'.format(media))
else:
    print('Infelizmente, você foi reprovado com média {:.2f}'.format(media))
