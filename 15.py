dias = int(input('Quantos dias de aluguel do carro? '))
km = float(input('Quantos kilimetros rodados? '))
total = (dias * 60) + (km * 0.15)
print ('O valor total ficou em R$ {:.2f}'.format(total))
