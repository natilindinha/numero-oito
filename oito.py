qmaiorq50peso60 = 0
alturainf150 = 0
olhosazuis = 0
pessoasruivas = 0
nazul = 0
pessoas = 0
q = 0
while pessoas <= 3:
    idade = int(input('digite sua idade: '))
    peso = str(input('digite seu peso: '))
    altura = str(input('digite sua altura: '))
    olhos = str(input('digite a cor de seus olhos: P-preto, A-azul, V- verde e C-castanho: '))
    cabelo = str(input('digite a cor de seu cabelo: P-preto, C-castanho, L-loiro, R-ruivo: '))
    if idade > 50 and peso < '60.0':
        qmaiorq50peso60 = qmaiorq50peso60 + 1
    if altura < '1,50' :
        alturainf150 = idade + alturainf150
        q = q + 1
    if olhos == 'A' or olhos == 'a':
        olhosazuis = olhosazuis + 1
    if (olhos != 'A' or olhos != 'a') and (cabelo == 'R' or cabelo == 'r'):
        nazul = nazul + 1
    pessoas = pessoas + 1

terra = alturainf150 / q
lavai = 6 * (olhosazuis / 100)
print("a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg é:", qmaiorq50peso60)
print("a média das pessoas com menos de 1,50 metros é de: ", terra, 'metros' )
print("a porcentagem de pessoas com os olhos azuis é de: ", lavai, "%" )
print("a quantidade de pessoas ruivas sem os olhos azuis é de: ", nazul)
