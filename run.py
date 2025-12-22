# run.py
import search
import time

# DEFINICIÓN DE LAS HERRAMIENTAS

def bfs_instrumented(problem): # problem: P_salida - P_meta - mapa
    return search.instrumented_graph_search(problem, search.FIFOQueue())


def dfs_instrumented(problem):
    return search.instrumented_graph_search(problem, search.Stack())


def bnb_instrumented(problem):
    return search.branch_and_bound_graph_search(problem)


def bnb_subestimation_instrumented(problem):
    return search.branch_and_bound_subestimation_graph_search(problem)

def brute_force_instrumented(problem):
    return search.brute_force_search(problem, search.FIFOQueue())


strategies = [
    ("Amplitud", bfs_instrumented),
    ("Profundidad", dfs_instrumented),
    ("Ramificación y Acotación", bnb_instrumented),
    ("R. y A. con Subestimación", bnb_subestimation_instrumented),
    ("Fuerza Bruta (Sin Memoria)", brute_force_instrumented)
]

# ---------------------------------------------------------------------
# 2. Casos de Prueba
# ---------------------------------------------------------------------
test_cases = [
    {"id": 1, "start": 'A', "goal": 'B', "label": "Arad -> Bucharest"},
    {"id": 2, "start": 'O', "goal": 'E', "label": "Oradea -> Eforie"},
    {"id": 3, "start": 'G', "goal": 'Z', "label": "Giurgiu -> Zerind"},
    {"id": 4, "start": 'N', "goal": 'D', "label": "Neamt -> Dobreta"},
    {"id": 5, "start": 'M', "goal": 'F', "label": "Mehadia -> Fagaras"}
]

# ---------------------------------------------------------------------
# 3. Ejecución con Medición de Tiempo (Alta Precisión)
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # Ajustamos el ancho de la columna TIEMPO para los nuevos decimales
    header = f"{'CASO':<20} | {'ESTRATEGIA':<25} | {'GEN':<5} | {'VIS':<5} | {'COST':<5} | {'TIEMPO (s)':<12} | {'RUTA'}"
    print(header)
    print("-" * len(header))

    for case in test_cases:
        problem = search.GPSProblem(case['start'], case['goal'], search.romania)

        print(f"\n--- ID {case['id']}: {case['label']} ---")

        for name, strategy in strategies:
            try:
                # 1. Tomamos el tiempo inicial con alta precisión
                # perf_counter usa el reloj del procesador, ideal para tiempos cortos
                start_time = time.perf_counter()

                # 2. Ejecutamos la búsqueda
                node, generated, visited = strategy(problem)

                # 3. Tomamos el tiempo final
                end_time = time.perf_counter()

                # 4. Calculamos la diferencia
                elapsed_time = end_time - start_time

                if node:
                    cost = node.path_cost
                    path_nodes = node.path()
                    path_str = str([n.state for n in path_nodes])
                else:
                    cost = "N/A"
                    path_str = "SIN SOLUCIÓN"
                    generated = 0
                    visited = 0

                # Formateamos el tiempo con 8 decimales para ver diferencias pequeñas
                time_str = f"{elapsed_time:.8f}"

                print(f"{name:<25} | {generated:<5} | {visited:<5} | {cost:<5} | {time_str:<12} | {path_str}")

            except Exception as e:
                print(f"{name:<25} | ERROR: {e}")

    print("\n" + "-" * len(header))