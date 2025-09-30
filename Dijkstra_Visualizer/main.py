# main.py

import pygame
import sys
from graph import Graph
from dijkstra import dijkstra_visualizer
import ui

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
NODE_RADIUS = 25
FONT_SIZE = 20

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dijkstra and Link-State Routing Visualizer")
font = pygame.font.SysFont("Arial", FONT_SIZE)
clock = pygame.time.Clock()

# --- Application State ---
graph = Graph()
source_node = None
node_count = 0
selected_node_for_edge = None
dijkstra_iterator = None
dijkstra_state = None
is_algorithm_running = False

# --- UI Elements ---
reset_button_rect = pygame.Rect(SCREEN_WIDTH - 160, 20, 140, 40)
run_button_rect = pygame.Rect(SCREEN_WIDTH - 160, 70, 140, 40)
step_button_rect = pygame.Rect(SCREEN_WIDTH - 160, 120, 140, 40)


def reset_visualization():
    """Resets the application to its initial state."""
    global graph, source_node, node_count, selected_node_for_edge
    global dijkstra_iterator, dijkstra_state, is_algorithm_running
    
    graph = Graph()
    source_node = None
    node_count = 0
    selected_node_for_edge = None
    dijkstra_iterator = None
    dijkstra_state = None
    is_algorithm_running = False


def main():
    """Main application loop."""
    global source_node, node_count, selected_node_for_edge
    global dijkstra_iterator, dijkstra_state, is_algorithm_running

    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Mouse Click Events
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                # Button Clicks
                if reset_button_rect.collidepoint(pos):
                        print("Reset button clicked")
                        reset_visualization()
                        continue
                
                    if run_button_rect.collidepoint(pos) and source_node and not is_algorithm_running:
                        print("Run button clicked")
                        is_algorithm_running = True
                        adj_list = graph.get_adjacency_list()
                        dijkstra_iterator = dijkstra_visualizer(adj_list, source_node)
                
                    if step_button_rect.collidepoint(pos) and dijkstra_iterator:
                        print("Step button clicked")
                        try:
                            dijkstra_state = next(dijkstra_iterator)
                        except StopIteration:
                            dijkstra_iterator = None # Algorithm finished
                
                # Graph Interaction
                clicked_on_node = None
                for node_id, node_pos in graph.nodes.items():
                    if (pos[0] - node_pos[0])**2 + (pos[1] - node_pos[1])**2 < NODE_RADIUS**2:
                        clicked_on_node = node_id
                        break
                
                if is_algorithm_running: continue # Disable graph edits while running

                # Left Click
                if event.button == 1: 
                    if clicked_on_node:
                        if not selected_node_for_edge:
                            selected_node_for_edge = clicked_on_node
                        else:
                            if selected_node_for_edge != clicked_on_node:
                                # Get weight for the new edge
                                weight_str = ui.get_input_box(screen, font, f"Enter weight for edge {selected_node_for_edge}-{clicked_on_node}:")
                                try:
                                    weight = int(weight_str)
                                    graph.add_edge(selected_node_for_edge, clicked_on_node, weight)
                                except (ValueError, TypeError):
                                    print("Invalid weight. Edge not added.")
                            selected_node_for_edge = None
                    else: # Create a new node
                        node_name = chr(ord('A') + node_count)
                        graph.add_node(node_name, pos)
                        node_count += 1
                        selected_node_for_edge = None

                # Right Click to select source node
                elif event.button == 3:
                    if clicked_on_node:
                        source_node = clicked_on_node
                        selected_node_for_edge = None

        # --- Drawing ---
        screen.fill(ui.COLORS['white'])
        
        # Draw edges
        for node1, neighbors in graph.edges.items():
            for node2, weight in neighbors.items():
                is_path = False
                # Highlight edges in the final shortest path tree
                if dijkstra_state and dijkstra_state['final_paths']:
                    paths = dijkstra_state['final_paths']
                    if (paths.get(node1) == node2) or (paths.get(node2) == node1):
                        is_path = True
                ui.draw_edge(screen, font, graph.nodes[node1], graph.nodes[node2], weight, ui.COLORS['gray'], is_path)

        # Draw nodes
        for node_id, pos in graph.nodes.items():
            color = ui.COLORS['blue']
            if node_id == source_node:
                color = ui.COLORS['orange']
            if node_id == selected_node_for_edge:
                color = ui.COLORS['yellow']

            distance = "inf"
            # Update colors and distances during visualization
            if dijkstra_state:
                dist_val = dijkstra_state['distances'].get(node_id)
                distance = str(dist_val) if dist_val is not None else "inf"
                
                if dijkstra_state['visited'] and node_id in dijkstra_state['visited']:
                    color = ui.COLORS['green']
                if dijkstra_state['current_node'] == node_id:
                    color = ui.COLORS['red']
            
            ui.draw_node(screen, font, pos, node_id, color, distance)

        # Draw Buttons and Text
        ui.draw_button(screen, font, reset_button_rect, "Reset", ui.COLORS['light_gray'])
        ui.draw_button(screen, font, run_button_rect, "Run", ui.COLORS['light_gray'])
        ui.draw_button(screen, font, step_button_rect, "Step", ui.COLORS['light_gray'])
        ui.draw_instructions(screen, font, SCREEN_WIDTH)

        # Draw Routing Table if algorithm is finished
        if dijkstra_state and not dijkstra_iterator:
            ui.draw_routing_table(screen, font, source_node, dijkstra_state['distances'], dijkstra_state['final_paths'])
            is_algorithm_running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()