import search
import time

def bfs_instrumented(problem):
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

test_cases = [
    {"id": 1, "start": 'A', "goal": 'B', "label": "Arad -> Bucharest"},
    {"id": 2, "start": 'O', "goal": 'E', "label": "Oradea -> Eforie"},
    {"id": 3, "start": 'G', "goal": 'Z', "label": "Giurgiu -> Zerind"},
    {"id": 4, "start": 'N', "goal": 'D', "label": "Neamt -> Dobreta"},
    {"id": 5, "start": 'M', "goal": 'F', "label": "Mehadia -> Fagaras"}
]



if __name__ == "__main__":
    header = f"{'CASO':<20} | {'ESTRATEGIA':<25} | {'GEN':<5} | {'VIS':<5} | {'COST':<5} | {'TIEMPO (s)':<12} | {'RUTA'}"
    print(header)
    print("-" * len(header))

    for case in test_cases:
        problem = search.GPSProblem(case['start'], case['goal'], search.romania)

        print(f"\n--- ID {case['id']}: {case['label']} ---")

        for name, strategy in strategies:
            try:
                # Utilizamos per_counter para obtener la precisión de la CPU
                start_time = time.perf_counter()
                node, generated, visited = strategy(problem)

                end_time = time.perf_counter()
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

                time_str = f"{elapsed_time:.8f}"

                print(f"{name:<25} | {generated:<5} | {visited:<5} | {cost:<5} | {time_str:<12} | {path_str}")

            except Exception as e:
                print(f"{name:<25} | ERROR: {e}")

    print("\n" + "-" * len(header))