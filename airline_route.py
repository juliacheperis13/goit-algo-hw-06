import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class AirlineRoute:
    routes = nx.Graph()
    
    def get_cities(self):
      return self.routes.nodes

    def add_connection(self, origin, destination, time):
        self.routes.add_edge(origin, destination, weight=time)
        print(
            f'Flight from {origin} to {destination} added. Estimated flight time: {time} hours.')

    def get_cities_number(self):
        cities_number = self.routes.number_of_nodes()
        print(f'Number of cities: {cities_number}')
        return cities_number

    def get_flights_number(self):
        flights_number = self.routes.number_of_edges()
        print(f'Flights number: {flights_number}')
        return flights_number

    def get_degree_centrality(self):
        degree_centrality = nx.degree_centrality(self.routes)
        print(f'Degree centrality: {degree_centrality}')
        return degree_centrality

    def get_closeness_centrality(self):
        closeness_centrality = nx.closeness_centrality(self.routes)
        print(f'Closeness centrality: {closeness_centrality}')
        return closeness_centrality

    def get_betweenness_centrality(self):
        betweenness_centrality = nx.betweenness_centrality(self.routes)
        print(f'Betweenness centrality: {betweenness_centrality}')
        return betweenness_centrality

    def draw_routes(self):
        pos = nx.spring_layout(self.routes, seed=42)
        nx.draw(self.routes, pos, with_labels=True, node_size=700,
                node_color="skyblue", font_size=11, width=2)
        labels = nx.get_edge_attributes(self.routes, 'weight')
        print(labels)
        nx.draw_networkx_edge_labels(self.routes, pos, edge_labels=labels)
        plt.show()

    def find_route_dfs(self, start_vertex):
        visited = set()
        # Використовуємо стек для зберігання вершин
        stack = [start_vertex]
        while stack:
            # Вилучаємо вершину зі стеку
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=' ')
                # Відвідуємо вершину
                visited.add(vertex)
                # Додаємо сусідні вершини до стеку
                stack.extend(reversed(list(self.routes.neighbors(vertex))))
        return visited

    def find_route_bfs(self, start_vertex):
        # Ініціалізація порожньої множини для зберігання відвіданих вершин
        visited = set()
        # Ініціалізація черги з початковою вершиною
        queue = deque([start_vertex])

        while queue:  # Поки черга не порожня, продовжуємо обхід
            # Вилучаємо першу вершину з черги
            vertex = queue.popleft()
            # Перевіряємо, чи була вершина відвідана раніше
            if vertex not in visited:
                # Якщо не була відвідана, друкуємо її
                print(vertex, end=" ")
                # Додаємо вершину до множини відвіданих вершин
                visited.add(vertex)
                # Додаємо всіх невідвіданих сусідів вершини до кінця черги
                # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
                queue.extend(set(list(self.routes.neighbors(vertex))) - visited)
        # Повертаємо множину відвіданих вершин після завершення обходу
        return visited
  
    def find_shortest_path(self, start):
        graph = self.routes
      
        distances = {vertex: float('infinity') for vertex in graph.nodes}
        distances[start] = 0
        unvisited = list(graph.nodes)

        while unvisited:
            # Знаходження вершини з найменшою відстанню серед невідвіданих
            current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

            # Якщо поточна відстань є нескінченністю, то ми завершили роботу
            if distances[current_vertex] == float('infinity'):
                break

            for neighbor in graph.neighbors(current_vertex):
                weight = graph[current_vertex][neighbor].get('weight', 1)
                distance = distances[current_vertex] + weight

                # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

            # Видаляємо поточну вершину з множини невідвіданих
            unvisited.remove(current_vertex)

        return distances