print ('Olá, vamos calcular quanta tinta será gasta para pintar a parede desejada.')
altura = int(input('Para isso eu preciso saber qual altura da parede: '))
largura = int(input('Agora digite a largura: '))
parede = altura * largura
tinta = parede / 2
print ('Você irá gastar {} litros de tinta para pintar a parede de {}m²'.format(tinta, parede))
