# Fazer um sistema que cadastra pessoas e mostra quem é mais velho/novo.

cadastro = []  # Lista vazia onde todos os cadastros serão guardados

while True:  # Inicia um loop infinito até o usuário decidir parar
    print('\n------Novo Cadastro------')

    nome = input('Digite seu nome: ')  # Recebe o nome da pessoa
    idade = int(input('Digite sua idade: '))  # Recebe a idade e converte para inteiro

    # Adiciona um novo dicionário dentro da lista cadastro
    # Cada dicionário representa uma pessoa com nome e idade
    cadastro.append({
        'Nome': nome,
        'Idade': idade,
    })

    # Pergunta se quer continuar cadastrando
    # .lower() converte a resposta para minúscula
    continuar = input('Deseja cadastrar outra pessoa? (s/n): ').lower()

    # Se a resposta for 'n', o loop é encerrado com break
    if continuar == 'n':
        break

# Após sair do while, começamos a parte de análise dos cadastros
print('\n------Todos os Cadastros------')

# o for percorre cada pessoa dentro da lista cadastro
for pessoa in cadastro:
    # Imprime o nome e idade de cada pessoa cadastrada
    print(f"Nome: {pessoa['Nome']} - Idade: {pessoa['Idade']}")

# Aqui usamos funções prontas do Python para achar o mais velho e o mais novo:
# max() → encontra o maior valor
# min() → encontra o menor valor
# key=lambda p: p['Idade'] diz que a comparação será feita usando a idade de cada pessoa

mais_velho = max(cadastro, key=lambda p: p['Idade'])  # Pega o dicionário da pessoa mais velha
mais_novo = min(cadastro, key=lambda p: p['Idade'])  # Pega o dicionário da pessoa mais nova

# Imprime a pessoa mais velha e mais nova
print(f"\nPessoa mais velha: {mais_velho['Nome']} ({mais_velho['Idade']} anos)")
print(f"Pessoa mais nova: {mais_novo['Nome']} ({mais_novo['Idade']} anos)")