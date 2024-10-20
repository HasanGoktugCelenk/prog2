
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r

import math as m
import random as r

def sphere_volume(n, d):
    # n is the number of random points
    # d is the number of dimensions of the sphere 

    # Generate n random points in d-dimensional space
    points = [
        [r.uniform(-1, 1) for _ in range(d)] 
        for _ in range(n)
    ]

    # Check how many points are inside the hypersphere
    inside_points = sum(
        1 for point in points if sum(x**2 for x in point) <= 1
    )
    
    # Volume approximation: Ratio of points inside hypersphere to total points * Volume of the cube
    volume_cube = 2 ** d
    estimated_volume = (inside_points / n) * volume_cube
    print(f"Approximate volume for d={d}, n={n}: {estimated_volume}")
    return estimated_volume

def hypersphere_exact(n, d):
    # Exact volume using the Gamma function
    # 'n' is ignored here since the exact calculation doesn't depend on it
    return (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)

def main():
    n = 100000
    d = 2

    # Compute the approximate volume using the Monte Carlo method
    approx_vol = sphere_volume(n, d)

    # Compute the exact volume using the formula
    exact_vol = hypersphere_exact(n, d)  # Pass n as well, but it will be ignored
    print(f"Exact volume for d={d}: {exact_vol}")

if __name__ == '__main__':
    main()
