# Dijkstra's Link-State Routing Visualizer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green?style=for-the-badge&logo=pygame)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

This project is an interactive educational tool designed to visualize Dijkstra's shortest path algorithm, demonstrating a core component of link-state routing protocols used in computer networks.

Users can dynamically build their own network topology and watch in real-time as the algorithm discovers the lowest-cost path from a source node to all other nodes. It's an ideal tool for students and enthusiasts looking to gain an intuitive understanding of complex networking concepts.

<p align="center">
  <img src="./demo.gif" alt="Animation of the Dijkstra Visualizer in action" width="800"/>
</p>

> **Note:** The animation above is a placeholder. The best way to showcase your project is to record a short GIF of it in action and name it `demo.gif`. You can upload it to your repository just like you uploaded the Python files.

---

## 🚀 Key Features

-   **Interactive Canvas**: Dynamically create network topologies by adding nodes (routers) and weighted edges (links) with your mouse.
-   **Step-by-Step Execution**: Control the algorithm's pace with a "Step" button to observe each decision it makes.
-   **Real-Time Visualization**: Nodes are color-coded to represent their state (unvisited, visited, current, source), and path costs are updated live on screen.
-   **Shortest Path Tree**: Once complete, the algorithm highlights the final shortest-path tree from the source.
-   **Routing Table Generation**: Automatically generates and displays the final routing table for the source node, showing destinations, total costs, and next hops.

---

## 🛠️ Installation & Setup

To get this project running on your local machine, follow these simple steps.

### **Prerequisites**

-   Python 3.8 or newer
-   Git

### **Installation Steps**

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/Dijkstra-Visualizer.git](https://github.com/YOUR_USERNAME/Dijkstra-Visualizer.git)
    cd Dijkstra-Visualizer
    ```
    *(Remember to replace `YOUR_USERNAME` with your actual GitHub username!)*

2.  **Create a Virtual Environment** (Recommended)
    This keeps your project dependencies isolated.
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    The `requirements.txt` file contains all the necessary Python packages.
    ```sh
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run

With the setup complete, start the application by running `main.py`:

```sh
python main.py
