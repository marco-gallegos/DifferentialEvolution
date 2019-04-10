from matplotlib import pyplot as plt
from ORM import Optimizacion

funciones = ["sphere", "rastring", "quartic", "rosenbrock"]


def plot(File_Name):
    dimensiones = [2, 4, 8 ,16]
    generacion_limite = 4000
    aumento_generacional = 100

    for dimension in dimensiones:
        x = []
        y = []
        generacion = 1
        while generacion < generacion_limite:
            data = Optimizacion.select().where((Optimizacion.generacion == generacion) & (Optimizacion.dimension == dimension) & (Optimizacion.funcion == File_Name))
            # print(data.sql())
            numero_registros = 0
            suma_fitnes = 0
            for row in data:
                suma_fitnes += row.fitness
                numero_registros += 1
            if suma_fitnes is 0:
                fitness_promedio = 0
            else:
                fitness_promedio = suma_fitnes / numero_registros
            x.append(generacion)
            y.append(fitness_promedio)
            generacion += aumento_generacional
        plt.plot(x, y, label=str(f"Dimension {dimension}"))
        plt.legend()
        plt.title(str(f"Solucion a Funcion {File_Name} Mediante DE"))
        plt.ylabel("Fitess")
        plt.xlabel("Generaciones")
    plt.show()


for funcion in funciones:
    plot(funcion)