class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino, costo):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, costo))

def dfs(grafo, nodo_actual, camino, costo_actual, costo_optimo):
    camino.append(nodo_actual)

    if nodo_actual == objetivo:
        if costo_actual < costo_optimo[0]:
            costo_optimo[0] = costo_actual
            mejor_camino = list(camino)
            print_info(camino, costo_actual, costo_optimo[0])
        return

    for vecino, costo in grafo.get(nodo_actual, []):
        print_info(camino, costo_actual, costo_optimo[0])
        dfs(grafo, vecino, camino, costo_actual + costo, costo_optimo)

    camino.pop()

def print_info(camino, costo_actual, costo_optimo):
    camino_str = ' -> '.join(camino)
    print(f"{camino_str}\t{costo_actual}\t{costo_optimo}")

# Ejemplo de uso:
grafo = Grafo()
grafo.agregar_arista('a', 'b', 5)
grafo.agregar_arista('b', 'e', 3)
grafo.agregar_arista('e', 'g', 1)
grafo.agregar_arista('a', 'c', 2)
grafo.agregar_arista('c', 'd', 4)

inicio = 'a'
objetivo = 'g'

print("Camino\t\tCosto Actual\tCosto Óptimo")
dfs(grafo.grafo, inicio, [], 0, [float('inf')])
