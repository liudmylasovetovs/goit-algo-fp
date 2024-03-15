import heapq


def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченні, крім початкової
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Ініціалізуємо бінарну купу для зберігання пар (відстань, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більша за відстань,
        # збережену в купі, пропускаємо цю вершину
        if current_distance > distances[current_vertex]:
            continue

        # Отримуємо список сусідів поточної вершини та їх відстаней
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань коротша за поточну відстань до сусіда,
            # оновлюємо відстань та додаємо сусіда до купи
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Приклад графа
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Найкоротші відстані від вершини", start_vertex)
for vertex, distance in shortest_distances.items():
    print(f"Від {start_vertex} до {vertex}: {distance}")
