from mapa import mapa_romenia, heuristica_bucareste


def exibir_fronteira(titulo, lista_nos):
    print()
    print(titulo)
    print(f"  {'f':>4} | {'g':>4} | {'h':>4} | {'Cidade':<15} | Caminho")
    print("  " + "-" * 55)
    for f, g, cidade, caminho in lista_nos:
        h = f - g
        print(f"  {f:>4} | {g:>4} | {h:>4} | {cidade:<15} | {' -> '.join(caminho)}")


inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

fronteira = [no_inicial]
print('Fronteira no começo:', fronteira)

no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no
print()
print('Nó retirado:', no)
print(' f =', f_atual, '| g =', g_atual, '| cidade =', cidade_atual,
      '| caminho =', caminho)
print('Fronteira agora:', fronteira)

for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

exibir_fronteira('Fronteira depois de expandir Arad (ordem de inserção):', fronteira)

fronteira.sort(key=lambda no: no[0])
exibir_fronteira('Fronteira ordenada pelo f (posição 0 da tupla):', fronteira)

proximo = fronteira.pop(0)
print()
print('Próximo nó a expandir:', proximo[2], 'com f =', proximo[0])

f_atual, g_atual, cidade_atual, caminho = proximo
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    if vizinho not in caminho:
        novo_g = g_atual + custo_estrada
        novo_h = heuristica_bucareste[vizinho]
        novo_f = novo_g + novo_h
        novo_caminho = caminho + [vizinho]
        fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

fronteira.sort(key=lambda no: no[0])
exibir_fronteira(f'Fronteira após expandir {cidade_atual} e reordenar:', fronteira)
print('\nNovo líder da fila:', fronteira[0][2], 'com f =', fronteira[0][0])