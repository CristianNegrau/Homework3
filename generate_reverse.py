# Exercitiu 6
# Generati toate numerele impare in ordine descrescatoare intre 999 si 901

odds = [i for i in range(900, 1000) if i % 2 != 0]
odds.reverse()

print(odds)
