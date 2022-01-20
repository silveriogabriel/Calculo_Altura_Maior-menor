'''Crie um programa que leia a altura de 10 alunos e seus numeros .. e no final mostre 
O maior e o menor aluno e seus numeros'''

#Definindo listas necessarias
numeroaluno = list()
alturaaluno = list()
maior = menor =  0

#Criando Laço de repetição para 10 alunos

for c in range(10):
    print('#---------------------------#')
    numeroaluno.append(int(input(f'Digite o numero do {c + 1} aluno: ')))
    alturaaluno.append(float(input(f'Digite a altura do aluno {c + 1}: ')))
    if c == 0:
        menor = alturaaluno[c]
        maior = alturaaluno[c]
    if alturaaluno[c] < menor:
        menor = alturaaluno[c]
    if alturaaluno[c] > maior:
        maior = alturaaluno[c]

#Pula_Linha

print()

#Laço para Mostrar alunos

for i, v in enumerate(alturaaluno):
    if menor == v:
        print(f'O aluno mais baixo foi o numero {numeroaluno[i]} com {alturaaluno[i]} de altura!')
    if maior == v:
        print(f'O aluno mais alto foi o numero {numeroaluno[i]} com {alturaaluno[i]} de altura!')
        
input()

        