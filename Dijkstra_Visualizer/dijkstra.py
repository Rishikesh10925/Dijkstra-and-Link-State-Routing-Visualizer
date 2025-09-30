# dijkstra.py

import heapq

def dijkstra_visualizer(graph, start_node):
    """
    A generator function that performs Dijkstra's algorithm step-by-step,
    yielding the state at each significant point for visualization.
    """
    # Initialize distances: 0 for the start node, infinity for all others
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    
    # Stores the previous node in the shortest path
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to store (distance, node) tuples
    pq = [(0, start_node)]
    
    visited = set()

    # Initial state yield
    yield {
        'current_node': None,
        'distances': distances.copy(),
        'visited': visited.copy(),
        'final_paths': None
    }

    while pq:
        # Get the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)

        # If we've already found a shorter path to this node, skip it
        if current_node in visited:
            continue
            
        # Mark the node as visited
        visited.add(current_node)

        # --- VISUALIZATION HOOK: After visiting a node ---
        # Yield the state to show which node is currently being processed
        yield {
            'current_node': current_node,
            'distances': distances.copy(),
            'visited': visited.copy(),
            'final_paths': None
        }

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                distance = current_distance + weight
                
                # If a shorter path is found to the neighbor
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
                    
                    # --- VISUALIZATION HOOK: After updating a distance ---
                    # Yield the state to show the updated distance
                    yield {
                        'current_node': current_node,
                        'distances': distances.copy(),
                        'visited': visited.copy(),
                        'final_paths': None
                    }

    # --- FINAL STATE YIELD ---
    # The algorithm is complete. Yield the final distances and paths.
    yield {
        'current_node': None,
        'distances': distances,
        'visited': visited,
        'final_paths': previous_nodes
    }