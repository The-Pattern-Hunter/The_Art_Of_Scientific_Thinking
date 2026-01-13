"""
Problem 1.6: Emergence - Boids Flocking Simulation
===================================================

This script demonstrates emergence through Reynolds' Boids algorithm.
Simple individual rules → Complex collective behavior (flocking)

Author: Dr. Alok Patel
Book: The Pattern Hunters - The Art of Scientific Thinking  
Chapter: 1 - The World as a Puzzle
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyArrowPatch
import seaborn as sns

sns.set_style("dark")

class Boid:
    """
    A single boid (bird-like agent) following three simple rules.
    """
    def __init__(self, position, velocity, color='blue'):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.color = color
        self.max_speed = 4.0
        self.max_force = 0.1
        
    def update(self, boids, width, height):
        """
        Update position based on three flocking rules.
        """
        # Apply three rules
        separation = self.separate(boids) * 1.5
        alignment = self.align(boids) * 1.0
        cohesion = self.cohere(boids) * 1.0
        
        # Apply forces
        self.velocity += separation + alignment + cohesion
        
        # Limit speed
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity = (self.velocity / speed) * self.max_speed
        
        # Update position
        self.position += self.velocity * 0.1
        
        # Wrap around boundaries (toroidal world)
        self.position[0] = self.position[0] % width
        self.position[1] = self.position[1] % height
    
    def separate(self, boids, desired_separation=15):
        """
        Rule 1: SEPARATION - Avoid crowding neighbors
        """
        steer = np.array([0.0, 0.0])
        count = 0
        
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if 0 < distance < desired_separation:
                # Calculate vector pointing away from neighbor
                diff = self.position - boid.position
                diff = diff / distance  # Weight by distance
                steer += diff
                count += 1
        
        if count > 0:
            steer = steer / count
        
        return steer
    
    def align(self, boids, neighbor_dist=50):
        """
        Rule 2: ALIGNMENT - Steer towards average heading of neighbors
        """
        sum_velocity = np.array([0.0, 0.0])
        count = 0
        
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if 0 < distance < neighbor_dist:
                sum_velocity += boid.velocity
                count += 1
        
        if count > 0:
            sum_velocity = sum_velocity / count
            # Desired velocity
            desired = sum_velocity
            # Steering = desired - current
            steer = desired - self.velocity
            # Limit force
            if np.linalg.norm(steer) > self.max_force:
                steer = (steer / np.linalg.norm(steer)) * self.max_force
            return steer
        
        return np.array([0.0, 0.0])
    
    def cohere(self, boids, neighbor_dist=50):
        """
        Rule 3: COHESION - Steer towards average position of neighbors
        """
        sum_position = np.array([0.0, 0.0])
        count = 0
        
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if 0 < distance < neighbor_dist:
                sum_position += boid.position
                count += 1
        
        if count > 0:
            sum_position = sum_position / count
            return self.seek(sum_position) * 0.01
        
        return np.array([0.0, 0.0])
    
    def seek(self, target):
        """
        Helper: Steer towards a target position
        """
        desired = target - self.position
        return desired


def create_flock(n_boids, width, height):
    """
    Create a flock of boids with random positions and velocities.
    """
    boids = []
    colors = plt.cm.viridis(np.linspace(0, 1, n_boids))
    
    for i in range(n_boids):
        x = np.random.random() * width
        y = np.random.random() * height
        angle = np.random.random() * 2 * np.pi
        speed = 2.0
        vx = speed * np.cos(angle)
        vy = speed * np.sin(angle)
        
        boid = Boid([x, y], [vx, vy], color=colors[i])
        boids.append(boid)
    
    return boids


def calculate_order_parameter(boids):
    """
    Calculate polarization (order parameter) of the flock.
    1.0 = perfect alignment, 0.0 = random directions
    """
    velocities = np.array([b.velocity for b in boids])
    avg_velocity = np.mean(velocities, axis=0)
    polarization = np.linalg.norm(avg_velocity) / np.mean([np.linalg.norm(v) for v in velocities])
    return polarization


def run_simulation(n_boids=50, width=200, height=200, frames=300, save_animation=True):
    """
    Run the flocking simulation.
    """
    print(f"\n🐦 Starting Boids Simulation")
    print(f"   Boids: {n_boids}")
    print(f"   Arena: {width}×{height}")
    print(f"   Frames: {frames}")
    print("=" * 70)
    
    # Create flock
    boids = create_flock(n_boids, width, height)
    
    # Setup figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Main simulation view
    ax1.set_xlim(0, width)
    ax1.set_ylim(0, height)
    ax1.set_aspect('equal')
    ax1.set_facecolor('#0a0a0a')
    ax1.set_title('Boids Flocking Simulation', fontsize=16, fontweight='bold', color='white')
    ax1.set_xlabel('Position X', fontsize=12, color='white')
    ax1.set_ylabel('Position Y', fontsize=12, color='white')
    ax1.tick_params(colors='white')
    
    # Prepare scatter plot
    positions = np.array([b.position for b in boids])
    colors = [b.color for b in boids]
    scat = ax1.scatter(positions[:, 0], positions[:, 1], 
                      c=colors, s=50, edgecolor='white', linewidth=0.5)
    
    # Velocity vectors (arrows)
    quiver = ax1.quiver(positions[:, 0], positions[:, 1],
                       [b.velocity[0] for b in boids],
                       [b.velocity[1] for b in boids],
                       color='yellow', alpha=0.6, width=0.003)
    
    # Order parameter plot
    ax2.set_xlim(0, frames)
    ax2.set_ylim(0, 1.1)
    ax2.set_facecolor('#f0f0f0')
    ax2.set_title('Emergence of Order', fontsize=16, fontweight='bold')
    ax2.set_xlabel('Time Step', fontsize=12)
    ax2.set_ylabel('Order Parameter (Polarization)', fontsize=12)
    ax2.axhline(y=0.9, color='red', linestyle='--', linewidth=2, 
                label='High Order (>0.9)', alpha=0.7)
    ax2.grid(True, alpha=0.3)
    
    # Data storage
    order_history = []
    time_steps = []
    
    # Text annotations
    info_text = ax1.text(0.02, 0.98, '', transform=ax1.transAxes,
                        fontsize=11, verticalalignment='top',
                        color='white', family='monospace',
                        bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    order_line, = ax2.plot([], [], 'b-', linewidth=2, label='Order Parameter')
    ax2.legend(fontsize=10)
    
    def animate(frame):
        """Animation update function."""
        # Update all boids
        for boid in boids:
            boid.update(boids, width, height)
        
        # Get new positions and velocities
        positions = np.array([b.position for b in boids])
        velocities = np.array([b.velocity for b in boids])
        
        # Update scatter plot
        scat.set_offsets(positions)
        
        # Update quiver
        quiver.set_offsets(positions)
        quiver.set_UVC(velocities[:, 0], velocities[:, 1])
        
        # Calculate order parameter
        order = calculate_order_parameter(boids)
        order_history.append(order)
        time_steps.append(frame)
        
        # Update order plot
        order_line.set_data(time_steps, order_history)
        
        # Update info text
        info = f"Frame: {frame}/{frames}\n"
        info += f"Boids: {n_boids}\n"
        info += f"Order: {order:.3f}\n"
        if order > 0.9:
            info += "Status: SYNCHRONIZED ✓"
        elif order > 0.7:
            info += "Status: Organizing..."
        else:
            info += "Status: Random"
        
        info_text.set_text(info)
        
        # Print progress
        if frame % 50 == 0:
            print(f"   Frame {frame:3d}: Order = {order:.3f}")
        
        return scat, quiver, info_text, order_line
    
    # Create animation
    print("\n⏳ Running simulation...")
    anim = FuncAnimation(fig, animate, frames=frames, 
                        interval=30, blit=True, repeat=True)
    
    # Save if requested
    if save_animation:
        print("💾 Saving animation (this may take a minute)...")
        try:
            anim.save('boids_emergence.gif', writer='pillow', fps=30)
            print("✓ Saved: boids_emergence.gif")
        except Exception as e:
            print(f"⚠ Could not save animation: {e}")
            print("  (Displaying instead)")
    
    plt.tight_layout()
    
    # Print final statistics
    print("\n📊 SIMULATION RESULTS")
    print("=" * 70)
    print(f"Initial Order: {order_history[0]:.3f} (random)")
    print(f"Final Order: {order_history[-1]:.3f}", end="")
    if order_history[-1] > 0.9:
        print(" (HIGHLY SYNCHRONIZED!)")
    elif order_history[-1] > 0.7:
        print(" (synchronized)")
    else:
        print(" (still organizing)")
    
    # Find when synchronization emerged
    high_order_frames = [i for i, o in enumerate(order_history) if o > 0.9]
    if high_order_frames:
        print(f"Time to synchronization: Frame {high_order_frames[0]}")
    
    print("\n💡 EMERGENCE DEMONSTRATED:")
    print("   • Simple rules (separation, alignment, cohesion)")
    print("   • No central coordinator")
    print("   • Complex behavior emerges from interactions")
    print("   • Order arises from chaos!")
    print("=" * 70)
    
    plt.show()
    
    return boids, order_history


def create_rules_diagram():
    """
    Create a visual explanation of the three boids rules.
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    rules = [
        {
            'title': 'Rule 1: SEPARATION',
            'description': 'Avoid crowding neighbors\n\n"Don\'t bump into others"',
            'color': 'red'
        },
        {
            'title': 'Rule 2: ALIGNMENT',
            'description': 'Match velocity of neighbors\n\n"Fly in same direction"',
            'color': 'blue'
        },
        {
            'title': 'Rule 3: COHESION',
            'description': 'Move toward center of neighbors\n\n"Stay with the group"',
            'color': 'green'
        }
    ]
    
    for ax, rule in zip(axes, rules):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Title
        ax.text(5, 9, rule['title'], ha='center', fontsize=16, 
                fontweight='bold', color=rule['color'])
        
        # Description
        ax.text(5, 7, rule['description'], ha='center', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    fig.suptitle('Three Simple Rules → Complex Flocking Behavior', 
                 fontsize=18, fontweight='bold')
    plt.tight_layout()
    plt.savefig('boids_rules.png', dpi=200, bbox_inches='tight')
    print("✓ Saved: boids_rules.png")
    plt.show()


def main():
    """
    Main function.
    """
    print("\n" + "=" * 70)
    print("EMERGENCE DEMONSTRATION: BOIDS FLOCKING ALGORITHM")
    print("=" * 70)
    print("\nThis simulation demonstrates EMERGENCE:")
    print("  • Individual agents follow 3 SIMPLE rules")
    print("  • NO central coordination")
    print("  • Complex FLOCKING behavior EMERGES")
    print("\nWatch as random chaos becomes organized order!")
    print("=" * 70)
    
    # Create rules diagram
    print("\n📐 Creating rules diagram...")
    create_rules_diagram()
    
    # Run simulation
    print("\n🎬 Starting main simulation...")
    boids, order_history = run_simulation(
        n_boids=60,
        width=200,
        height=200,
        frames=300,
        save_animation=True
    )
    
    print("\n✅ Simulation complete!")
    print("\n🎓 KEY LESSON:")
    print("   Emergence = whole > sum of parts")
    print("   Simple rules → Complex behavior")
    print("   This is how nature works: ants, neurons, cells!")

if __name__ == "__main__":
    main()
