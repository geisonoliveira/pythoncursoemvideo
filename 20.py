from random import shuffle
pri = input("Digite o primeiro aluno: ")
seg = input("Digite o segundo aluno: ")
ter = input("Digite o terceiro aluno: ")
quar = input("Digite o quarto aluno: ")
lista = [pri, seg, ter, quar]
shuffle(lista)
print ("A ordem de apresentação será: {}".format(lista))
