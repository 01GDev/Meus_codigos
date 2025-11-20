# Meus_codigos
Codigos_iniciais
print('----Controle de estoque----')
estoque = []

while True:
    Produto = input("Digite o nome do produto: ")
    Qnt = int(input("Digite a quantidade do produto: "))
    
    estoque.append({"Produto": Produto, "Quantidade": Qnt})
    
    continuar = input("Deseja cadastrar mais produtos S/N: ").lower()
    
    if continuar == "n":
        break

    
print("----TODOS OS PRODUTOS----")
for item in estoque:
    print(item)
    
maior = max(estoque, key=lambda x: x["Quantidade"])
print("Produto com MAIOR quantidade:")
print(f"produto: {maior['Produto']} | Quantidade: {maior['Quantidade']}")
