# Programa para classificar nadadores por idade

# Pede a idade do nadador
idade = int(input("Digite a idade do nadador: "))

# Verifica a categoria
if idade >= 5 and idade <= 7:
    print("Categoria: Infantil")
elif idade >= 8 and idade <= 17:
    print("Categoria: Juvenil")
elif idade >= 18:
    print("Categoria: Adulto")
else:
    print("Idade inválida para classificação")