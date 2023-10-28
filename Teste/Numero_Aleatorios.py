import urandom # Importa a biblioteca

# Gerar um nmero pseudoaleatrio entre 0 e 9
random_bits = urandom.getrandbits(4)  # 4 bits geram numeros de 0 a 15
numero = random_bits % 11  # Reduzir para o intervalo de 0 a 9

print()
print()
print(numero) # Imprime o numero sorteado
print()