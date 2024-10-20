
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import concurrent.futures
import time

# Define pc as an alias for time.perf_counter
pc = time.perf_counter

# Original function to approximate hypersphere volume
def sphere_volume(n, d):
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
    return estimated_volume

# Exact volume function
def hypersphere_exact(n, d):
    return (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)

# Part 1: Parallelizing the loop
def sphere_volume_parallel1(n, d, np):
    with concurrent.futures.ProcessPoolExecutor(max_workers=np) as executor:
        # Using the executor to run 10 instances of sphere_volume(n, d) in parallel
        results = list(executor.map(sphere_volume, [n]*10, [d]*10))
    
    # Average the results to get a single float value
    return sum(results) / len(results)

# Part 2: Parallelizing the actual computations by splitting data
def sphere_volume_parallel2(n, d, np):
    # Split n into np parts for parallel computation
    n_per_process = n // np
    with concurrent.futures.ProcessPoolExecutor(max_workers=np) as executor:
        # Each process gets n_per_process random points
        results = list(executor.map(sphere_volume, [n_per_process]*np, [d]*np))
    
    # Combine results from all processes (average the estimated volumes)
    combined_volume = sum(results) / np
    return combined_volume

def main():
    n = 100000
    d = 11
    np = 10  # Number of processes

    # Sequential version (timed)
    start = pc()
    for _ in range(10):
        sphere_volume(n, d)
    sequential_duration = pc() - start
    print(f"Sequential version took {sequential_duration:.4f} seconds")

    # Part 1: Parallelizing the loop
    start = pc()
    results_parallel1 = sphere_volume_parallel1(n, d, np)
    parallel1_duration = pc() - start
    print(f"Parallelized loop version took {parallel1_duration:.4f} seconds")
    print(f"Approximate volume (parallel1): {results_parallel1}")
    
    # Part 2: Parallelizing the computation
    start = pc()
    results_parallel2 = sphere_volume_parallel2(n, d, np)
    parallel2_duration = pc() - start
    print(f"Parallelized computation version took {parallel2_duration:.4f} seconds")
    print(f"Approximate volume (parallel2): {results_parallel2}")

if __name__ == '__main__':
    main()
