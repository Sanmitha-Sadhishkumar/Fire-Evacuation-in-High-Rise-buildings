import numpy as np
import matplotlib.pyplot as plt
# Define Social Force Model parameters
repulsion_strength = 2.0
repulsion_range = 1.0
time_step = 0.1  # Time step for simulation

# Speed ratios for different types of pedestrians
speed_ratios = {
    'child': 1.0,
    'adult': 2.0,
    'elderly': 1.0
}

class Pedestrian:
    def __init__(self, position, destination, p_type='adult'):
        # Convert position and destination to float arrays to avoid type mismatch
        self.position = np.array(position, dtype=float)
        self.destination = np.array(destination, dtype=float)
        self.velocity = np.zeros(2, dtype=float)  # Ensure velocity is float
        self.type = p_type
        self.desired_speed = speed_ratios[self.type]  # Set speed based on pedestrian type

    def update_velocity(self, obstacles):
        # Attractive force toward destination
        direction = self.destination - self.position
        norm = np.linalg.norm(direction)
        if norm != 0:
            direction /= norm  # Normalize direction vector
        attractive_force = self.desired_speed * direction

        # Repulsive force from obstacles
        repulsive_force = np.zeros(2)
        for obs in obstacles:
            obstacle_direction = self.position - obs
            distance = np.linalg.norm(obstacle_direction)
            if distance < repulsion_range and distance != 0:
                obstacle_direction /= distance  # Normalize
                # Repulsion strength decreases with distance
                repulsive_force += repulsion_strength * (1 / distance - 1 / repulsion_range) * obstacle_direction

        self.velocity = attractive_force + repulsive_force

    def update_position(self):
        self.position += self.velocity * time_step

    def get_speed(self):
        return np.linalg.norm(self.velocity)

def simulate_crowd(pedestrians, obstacles, num_steps):
    plt.figure(figsize=(5, 5))
    for step in range(num_steps):
        for p in pedestrians:
            p.update_velocity(obstacles)
            p.update_position()

        plot_crowd(pedestrians, obstacles)
        plt.savefig(f'../static/sfm{step}.png')
        plt.pause(0.1) 

def plot_crowd(pedestrians, obstacles):
    plt.clf() 
    for i, p in enumerate(pedestrians):
        plt.plot(p.position[0], p.position[1], 'ro')
        speed = p.get_speed()
        plt.text(p.position[0] + 0.1, p.position[1], f'{p.type.capitalize()} Speed: {speed:.2f}', fontsize=9, color='black')

    for obs in obstacles:
        plt.plot(obs[0], obs[1], 'bs', markersize=10) 

    plt.xlim(0, 10)
    plt.ylim(0, 10)

def social_forces_predict():
    pedestrians = [
    Pedestrian(position=[0, 0], destination=[8, 8], p_type='child'),
    Pedestrian(position=[1, 1], destination=[8, 8], p_type='adult'),
    Pedestrian(position=[2, 2], destination=[8, 8], p_type='elderly'),
    Pedestrian(position=[0.5, 0], destination=[8, 8], p_type='child'),
    Pedestrian(position=[1.5, 1.5], destination=[8, 8], p_type='adult')
    ]

    obstacles = [
    [4, 4], 
    [6, 6], 
    [5, 3], 
    ]

    simulate_crowd(pedestrians, obstacles, num_steps=100)
    plt.savefig('../static/sfm.png')