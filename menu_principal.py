"""
menu_principal.py
Proyecto Estructura de Datos II - Grafos
Menú principal del programa.
"""

from grafo import Grafo


def cargar_ejemplo(g):
    """Grafo de ejemplo para probar el programa."""
    aristas = [("A", "B", 4), ("A", "C", 2), ("B", "D", 5), ("C", "D", 8),
               ("C", "E", 10), ("D", "E", 2), ("D", "F", 6), ("E", "F", 3)]
    for origen, destino, peso in aristas:
        g.agregar_arista(origen, destino, peso)


def pedir_vertice(g, mensaje):
    vertice = input(mensaje).strip().upper()
    if not g.buscar_vertice(vertice):
        print(f"El vértice '{vertice}' no existe en el grafo.")
        return None
    return vertice


def menu():
    g = Grafo()
    cargar_ejemplo(g)

    while True:
        print("\n===== MENÚ DE GRAFOS =====")
        print("1. Mostrar grafo")
        print("2. Agregar vértice")
        print("3. Agregar arista")
        print("4. Recorrido en anchura (BFS)")
        print("5. Recorrido en profundidad (DFS)")
        print("6. Buscar vértice")
        print("7. Distancia entre dos nodos")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print("Grafo (vértice -> vecino(peso)):")
            g.mostrar()

        elif opcion == "2":
            v = input("Nombre del vértice: ").strip().upper()
            if v and g.agregar_vertice(v):
                print(f"Vértice '{v}' agregado.")
            else:
                print("El vértice ya existe o el nombre está vacío.")

        elif opcion == "3":
            origen = input("Vértice origen: ").strip().upper()
            destino = input("Vértice destino: ").strip().upper()
            try:
                peso = float(input("Peso de la arista: "))
                if peso.is_integer():
                    peso = int(peso)
            except ValueError:
                print("El peso debe ser un número.")
                continue
            if origen and destino:
                g.agregar_arista(origen, destino, peso)
                print(f"Arista {origen} - {destino} con peso {peso} agregada.")

        elif opcion == "4":
            inicio = pedir_vertice(g, "Nodo inicial: ")
            if inicio:
                print("Recorrido en anchura:", " -> ".join(g.recorrido_anchura(inicio)))

        elif opcion == "5":
            inicio = pedir_vertice(g, "Nodo inicial: ")
            if inicio:
                print("Recorrido en profundidad:", " -> ".join(g.recorrido_profundidad(inicio)))

        elif opcion == "6":
            v = input("Vértice a buscar: ").strip().upper()
            encontrado = g.buscar_vertice(v)
            print(f"Resultado: {encontrado}")
            print(f"El vértice '{v}' {'SÍ' if encontrado else 'NO'} se encuentra en el grafo.")

        elif opcion == "7":
            origen = pedir_vertice(g, "Nodo origen: ")
            if not origen:
                continue
            destino = pedir_vertice(g, "Nodo destino: ")
            if not destino:
                continue
            camino, total = g.distancia(origen, destino)
            if camino is None:
                print(f"No existe un camino entre {origen} y {destino}.")
            else:
                print("Camino encontrado:", " -> ".join(camino))
                print(f"Distancia (suma de pesos): {total}")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()