from airline_route import AirlineRoute

# OSL - Oslo
# WAW - Warsaw
# LIS - Lisboa
# BCN - Barcelona
# AMS - Amsterdam
# KEF - Keflavik
# CDG - Paris


def main():
    routes = AirlineRoute()

    routes.add_connection('WAW', 'OSL', 2)
    routes.add_connection('WAW', 'CDG', 2.3)
    routes.add_connection('WAW', 'LIS', 4.2)
    routes.add_connection('WAW', 'KEF', 2.7)

    routes.add_connection('OSL', 'KEF', 3)
    routes.add_connection('OSL', 'BCN', 3.5)
    routes.add_connection('OSL', 'LIS', 4)
    routes.add_connection('OSL', 'CDG', 4)

    routes.add_connection('AMS', 'BCN', 2)
    routes.add_connection('AMS', 'CDG', 1.2)
    
    routes.get_cities_number()
    routes.get_flights_number()
    
    routes.get_degree_centrality()
    routes.get_betweenness_centrality()
    routes.get_closeness_centrality()
    
    routes.draw_routes()
    
    print('BFS')
    routes.find_route_bfs('WAW')

    print('DFS')
    routes.find_route_dfs('WAW')

    for city in routes.get_cities():
        print(f'City {city}, distances: {routes.find_shortest_path(city)}')


if __name__ == "__main__":
    main()
