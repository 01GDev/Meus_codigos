senha = '1234'
tentativas = 0

while tentativas <3:
	s_d = input('digite sua senha')
	if s_d == senha:
		print('acesso liberado')
		break
		
	else: 
	 tentativas += 1
	 
	 
if tentativas == 3:
	print('acesso negado')