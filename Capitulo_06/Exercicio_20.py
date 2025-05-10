versao_original = [1, 2, 3, 4, 5]
versao_alterada = [3, 4, 5, 6, 7]

original_set = set(versao_original)
alterada_set = set(versao_alterada)

nao_mudaram = original_set & alterada_set
print("Elementos que não mudaram:", list(nao_mudaram))

novos_elementos = alterada_set - original_set
print("Novos elementos:", list(novos_elementos))

removidos = original_set - alterada_set
print("Elementos removidos:", list(removidos))
