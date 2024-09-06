string_original = "Exemplo de string"

invertida = ''
for i in range(len(string_original) - 1, -1, -1):
    invertida += string_original[i]

print(invertida)
