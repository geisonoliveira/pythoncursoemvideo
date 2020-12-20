preco = int(input('Qual valor do produto ao qual deseja desonto? '))
desconto = preco * 5 / 100
valorfinal = preco - desconto
print ('O produto vai custar somente R$ {:.2f} com 5% de desconto da loja.'.format(valorfinal))