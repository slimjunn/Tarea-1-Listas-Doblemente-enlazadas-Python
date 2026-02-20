from graphviz import Digraph
import os

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.carnet})"


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.generar_grafica("insertar_principio")

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
        self.generar_grafica("insertar_final")

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza

        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior

                print("Nodo eliminado correctamente.")
                self.generar_grafica("eliminar")
                return

            actual = actual.siguiente

        print("No se encontró un nodo con ese carnet.")

    def mostrar_lista(self):
        actual = self.cabeza
        resultado = "None <- "

        while actual:
            resultado += f"[{actual}] <-> "
            actual = actual.siguiente

        resultado += "None"
        print(resultado)

    def generar_grafica(self, operacion):
        if not os.path.exists("imagenes"):
            os.makedirs("imagenes")

        dot = Digraph()
        dot.attr(rankdir='LR')

        actual = self.cabeza
        contador = 0

        while actual:
            nombre_nodo = f"N{contador}"
            etiqueta = f"{actual.nombre}\n{actual.apellido}\n{actual.carnet}"
            dot.node(nombre_nodo, etiqueta)

            if actual.siguiente:
                dot.edge(nombre_nodo, f"N{contador+1}")
                dot.edge(f"N{contador+1}", nombre_nodo)

            actual = actual.siguiente
            contador += 1

        dot.render(f"imagenes/lista_{operacion}", format="png", cleanup=True)
