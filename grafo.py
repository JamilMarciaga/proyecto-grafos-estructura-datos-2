"""
grafo.py
Clase Grafo: lista de adyacencia con pesos, recorridos en anchura y profundidad,
búsqueda de vértice y distancia entre dos nodos basada en el recorrido en anchura.
"""

from collections import deque


class Grafo:
    def __init__(self, dirigido=False):
        # Lista de adyacencia: {vertice: {vecino: peso}}
        self.adyacencia = {}
        self.dirigido = dirigido

    # ---------- Operaciones básicas ----------
    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = {}
            return True
        return False

    def agregar_arista(self, origen, destino, peso):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen][destino] = peso
        if not self.dirigido:
            self.adyacencia[destino][origen] = peso

    def mostrar(self):
        if not self.adyacencia:
            print("El grafo está vacío.")
            return
        for vertice, vecinos in self.adyacencia.items():
            conexiones = ", ".join(f"{v}({p})" for v, p in vecinos.items())
            print(f"  {vertice} -> {conexiones if conexiones else 'sin conexiones'}")

    # ---------- a. Recorrido en anchura (BFS) ----------
    def recorrido_anchura(self, inicio):
        """Visita los nodos por niveles usando una COLA (FIFO)."""
        visitados = [inicio]
        cola = deque([inicio])
        while cola:
            actual = cola.popleft()
            for vecino in self.adyacencia[actual]:
                if vecino not in visitados:
                    visitados.append(vecino)
                    cola.append(vecino)
        return visitados

    # ---------- b. Recorrido en profundidad (DFS) ----------
    def recorrido_profundidad(self, inicio):
        """Avanza lo más lejos posible por cada camino usando una PILA (LIFO)."""
        visitados = []
        pila = [inicio]
        while pila:
            actual = pila.pop()
            if actual not in visitados:
                visitados.append(actual)
                # Se apilan en orden inverso para visitar los vecinos en el orden en que se agregaron
                for vecino in reversed(list(self.adyacencia[actual])):
                    if vecino not in visitados:
                        pila.append(vecino)
        return visitados

    # ---------- c. Buscar vértice ----------
    def buscar_vertice(self, vertice):
        """Retorna True si el vértice existe en el grafo, False en caso contrario."""
        return vertice in self.adyacencia

    # ---------- d. Distancia entre dos nodos (basada en BFS) ----------
    def distancia(self, origen, destino):
        """
        Usa el recorrido en anchura para encontrar el camino de origen a destino
        y suma los pesos de los arcos de ese camino.
        Retorna (camino, distancia) o (None, None) si no hay camino.
        """
        padre = {origen: None}
        cola = deque([origen])
        while cola:
            actual = cola.popleft()
            if actual == destino:
                break
            for vecino in self.adyacencia[actual]:
                if vecino not in padre:
                    padre[vecino] = actual
                    cola.append(vecino)

        if destino not in padre:
            return None, None

        # Reconstruir el camino desde el destino hasta el origen
        camino = []
        nodo = destino
        while nodo is not None:
            camino.append(nodo)
            nodo = padre[nodo]
        camino.reverse()

        # Sumar los pesos de los arcos del camino
        total = 0
        for i in range(len(camino) - 1):
            total += self.adyacencia[camino[i]][camino[i + 1]]
        return camino, total