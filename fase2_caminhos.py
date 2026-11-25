from mapa import mapa_romenia, heuristica_bucareste


def custo_da_estrada(origem, destino):
    """Devolve os km da estrada origem -> destino, ou None se ela não existe."""
    if origem not in mapa_romenia:
        return None
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None


def caminho_valido(caminho):
    """Verifica se todas as conexões entre as cidades do caminho realmente existem."""
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if custo_da_estrada(caminho[i], caminho[i + 1]) is None:
            return False
    return True


def custo_do_caminho(caminho):
    """Recebe uma lista de cidades e devolve a soma das estradas, em km (ou None se inválido)."""
    if not caminho_valido(caminho):
        return None
    total = 0
    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    return total


print("Arad -> Sibiu custa", custo_da_estrada("Arad", "Sibiu"), "km")
print("Arad -> Bucharest custa", custo_da_estrada("Arad", "Bucharest"), "(não existe estrada direta)")

por_fagaras = ["Arad", "Sibiu", "Fagaras", "Bucharest"]
por_pitesti = ["Arad", "Sibiu", "Rimnicu Vilcea", "Pitesti", "Bucharest"]

print()
print("Caminho por Fagaras:", " -> ".join(por_fagaras))
print("  custo =", custo_do_caminho(por_fagaras), "km")
print("Caminho por Pitesti:", " -> ".join(por_pitesti))
print("  custo =", custo_do_caminho(por_pitesti), "km")


def mostrar_g_h_f(caminho):
    """Para cada cidade do caminho imprime g (já andado), h (falta) e f = g + h."""
    if not caminho_valido(caminho):
        print("Caminho inválido: existe um trecho sem estrada direta.")
        return
    print(f"  {'cidade':<15} {'g(n)':>5} {'h(n)':>5} {'f(n)':>5}")
    for i in range(len(caminho)):
        cidade = caminho[i]
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h
        print(f"  {cidade:<15} {g:>5} {h:>5} {f:>5}")


print()
print("Valores ao longo do caminho por Fagaras:")
mostrar_g_h_f(por_fagaras)

print()
print("Valores ao longo do caminho por Pitesti:")
mostrar_g_h_f(por_pitesti)


# --- Adição: Comparação automática entre os caminhos ---
def comparar_caminhos(rotas):
    """Compara uma lista de rotas válidas e destaca a mais curta."""
    validas = [(r, custo_do_caminho(r)) for r in rotas if caminho_valido(r)]
    if not validas:
        return
    melhor_rota, menor_custo = min(validas, key=lambda item: item[1])
    pior_custo = max(validas, key=lambda item: item[1])[1]
    economia = pior_custo - menor_custo

    print()
    print("--- Resumo da Comparação ---")
    print("Melhor caminho:", " -> ".join(melhor_rota))
    print(f"Menor custo total: {menor_custo} km (economia de {economia} km)")


comparar_caminhos([por_fagaras, por_pitesti])