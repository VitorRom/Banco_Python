# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicitar os itens ao usuário:
for _ in range(3):
    item = input("Digite o seu item: ")
    itens.append(item)

# Exibe a lista de itens
print("\nLista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
