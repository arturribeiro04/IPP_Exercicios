primeira = "CTA"
segunda = "ABC" 
terceira = None

conjunto_um = set(primeira)
conjunto_dois = set(segunda)

comparacao_um = conjunto_um - conjunto_dois
comparacao_dois = conjunto_dois - conjunto_um

terceira = "".join(comparacao_um) + "".join(comparacao_dois)

print(terceira)