from random import sample

quant_jogos = int(input('Digite quantidade de jogos: '))
quant_num = int(input('Digite quantidade de números: '))
num_alto = int(input('Digite número mais alto da cartela: '))
i = 0

while i < quant_jogos:
    lista = sample(range(1,num_alto),quant_num)
    form_megasena = str(lista).replace(', ','-').strip('[]')
    print(form_megasena)
    with open ('sorteio.txt', 'a') as arquivo:
        arquivo.write("%s\n" % form_megasena)
    i +=1
