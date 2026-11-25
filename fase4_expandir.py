from mapa import mapa_romenia, heuristica_bucareste


def mostrar_fronteira(fronteira):
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    print('   fronteira:', ', '.join(partes) if partes else '(vazia)')


def expandir(no, explorados):
    f_atual, g_atual, cidade_atual, caminho = no
    filhos = []
    for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
        if vizinho in explorados:
            continue
        novo_g = g_atual + custo_estrada
        novo_f = novo_g + heuristica_bucareste[vizinho]
        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
    return filhos


inicio = 'Arad'
destino = 'Bucharest'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

for rodada in:
    if not fronteira:
        break
    fronteira.sort(key=lambda no: no)
    no = fronteira.pop(0)
    f, g, cidade, caminho = no

    print(f'Rodada {rodada}: expandindo {cidade} (f={f}, g={g})')
    print('   caminho atual:', ' -> '.join(caminho))

    if cidade == destino:
        print(f'   Destino {destino} alcançado com custo total de {g} km!')
        break

    explorados.add(cidade)
    fronteira = fronteira + expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('   explorados:', sorted(explorados))
    print()