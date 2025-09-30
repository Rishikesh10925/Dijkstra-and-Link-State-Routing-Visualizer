# ui.py

import pygame
import sys

# --- Color Constants ---
COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (200, 200, 200),
    'light_gray': (220, 220, 220),
    'blue': (50, 150, 255),
    'green': (0, 200, 100),
    'red': (255, 100, 100),
    'orange': (255, 165, 0),
    'yellow': (255, 255, 0),
    'path_highlight': (255, 20, 147) # Deep Pink
}

NODE_RADIUS = 25

def draw_node(surface, font, pos, name, color, distance):
    """Draws a single node (router)."""
    pygame.draw.circle(surface, color, pos, NODE_RADIUS)
    pygame.draw.circle(surface, COLORS['black'], pos, NODE_RADIUS, 2)
    
    # Draw node name
    text_surf = font.render(name, True, COLORS['black'])
    text_rect = text_surf.get_rect(center=pos)
    surface.blit(text_surf, text_rect)
    
    # Draw distance
    dist_surf = font.render(distance, True, COLORS['black'])
    dist_rect = dist_surf.get_rect(center=(pos[0], pos[1] + NODE_RADIUS + 10))
    surface.blit(dist_surf, dist_rect)

def draw_edge(surface, font, pos1, pos2, weight, color, is_path=False):
    """Draws a single edge (link) with its weight."""
    line_width = 5 if is_path else 2
    line_color = COLORS['path_highlight'] if is_path else COLORS['black']
    pygame.draw.line(surface, line_color, pos1, pos2, line_width)
    
    # Draw weight
    mid_pos = ((pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2)
    weight_surf = font.render(str(weight), True, COLORS['black'])
    weight_rect = weight_surf.get_rect(center=mid_pos)
    pygame.draw.rect(surface, COLORS['white'], weight_rect.inflate(4, 4)) # Background for text
    surface.blit(weight_surf, weight_rect)

def draw_button(surface, font, rect, text, color):
    """Draws a clickable button."""
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, COLORS['black'], rect, 2)
    text_surf = font.render(text, True, COLORS['black'])
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

def draw_instructions(surface, font, screen_width):
    """Displays usage instructions."""
    instructions = [
        "Instructions:",
        "Left Click: Add a node",
        "Left Click Node -> Left Click Node: Add an edge",
        "Right Click Node: Select source",
        "---",
        "Color Key:",
        "Orange: Source Node",
        "Red: Current Node",
        "Green: Visited Node",
        "Yellow: Selected for Edge"
    ]
    y_offset = 200
    for line in instructions:
        text_surf = font.render(line, True, COLORS['black'])
        surface.blit(text_surf, (screen_width - 200, y_offset))
        y_offset += 25

def get_next_hop(paths, source, dest):
    """Finds the next hop router on the path from source to dest."""
    if paths[dest] is None or dest == source:
        return "-"
    path_node = dest
    while paths[path_node] is not None and paths[path_node] != source:
        path_node = paths[path_node]
    return path_node

def draw_routing_table(surface, font, source, distances, paths):
    """Draws the final routing table for the source node."""
    table_x, table_y = 40, 40
    header = f"Routing Table for Source Node: {source}"
    header_surf = font.render(header, True, COLORS['black'])
    surface.blit(header_surf, (table_x, table_y))
    
    # Table headers
    y_offset = table_y + 40
    headers = ["Destination", "Cost", "Next Hop"]
    for i, h in enumerate(headers):
        text_surf = font.render(h, True, COLORS['black'])
        surface.blit(text_surf, (table_x + i * 120, y_offset))
    y_offset += 30

    # Table rows
    sorted_nodes = sorted(distances.keys())
    for node in sorted_nodes:
        if node == source: continue
        cost = distances[node]
        next_hop = get_next_hop(paths, source, node)
        
        row_data = [node, str(cost), next_hop]
        for i, data in enumerate(row_data):
            text_surf = font.render(data, True, COLORS['black'])
            surface.blit(text_surf, (table_x + i * 120, y_offset))
        y_offset += 25

def get_input_box(screen, font, prompt):
    """A simple blocking function to get text input from the user."""
    input_text = ""
    input_active = True
    # Center the input box on the screen
    prompt_rect = pygame.Rect(0, 0, 500, 100)
    prompt_rect.center = screen.get_rect().center
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Draw the input box
        pygame.draw.rect(screen, COLORS['light_gray'], prompt_rect)
        pygame.draw.rect(screen, COLORS['black'], prompt_rect, 2)
        
        prompt_surf = font.render(prompt, True, COLORS['black'])
        screen.blit(prompt_surf, (prompt_rect.x + 10, prompt_rect.y + 10))
        
        input_surf = font.render(input_text, True, COLORS['black'])
        screen.blit(input_surf, (prompt_rect.x + 10, prompt_rect.y + 50))
        
        pygame.display.flip()
        
    return input_text