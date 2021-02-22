from math import cos, sin, tan, radians
angulo = float(input("Digite um angulo "))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tan= tan(radians(angulo))
print ("O cosseno do angulo é {:.2f}, seu seno é {:.2f} e sua tangente é {:.2f}".format(cosseno, seno, tan))
