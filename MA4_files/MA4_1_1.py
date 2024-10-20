
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""


import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    for _ in range(n):
        x, y = r.uniform(-1, 1), r.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = (inside_circle / n) * 4

    # Plot the points
    plt.figure(figsize=(5, 5))
    plt.scatter(x_inside, y_inside, color='blue', s=1)
    plt.scatter(x_outside, y_outside, color='red', s=1)
    plt.title(f"Monte Carlo Approximation of π with {n} points: π ≈ {pi_estimate}")
    plt.gca().set_aspect('equal')
    plt.show()

    return pi_estimate
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
