from math import hypot
catopot = float(input("Digite o valor do cateto oposto do triangulo retangulo "))
catadj = float(input("Agora digite o valor do cateto adjacente do triangulo retangulo "))
hip = hypot(catopot, catadj)
print ("O valor da hipotenusa é de {:.2f}".format(hip))
