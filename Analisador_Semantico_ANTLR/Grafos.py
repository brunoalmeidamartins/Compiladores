from collections import defaultdict

class Grafo(object):
    def __init__(self):
        self._data = defaultdict(list)

    def conectar(self, nodo_origem, nodo_destino):
        self._data[nodo_origem].append(nodo_destino)

    def vizinhos(self, nodo):
        return self._data[nodo]

    def verificar_ciclos(self, nodo_inicial):
        nodos_visitados = set()
        nodos_restantes = [nodo_inicial]

        while nodos_restantes:
            nodo_atual = nodos_restantes.pop()
            nodos_visitados.add(nodo_atual)

            for vizinho in self.vizinhos(nodo_atual):
                if vizinho in nodos_visitados:
                    return True

                nodos_restantes.append(vizinho)

        return False
