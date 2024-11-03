#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1300 Lab 2 Code
Section 1: Calculation of e-array from analytical results

Section 2: Plotting of array. 
"""
#Imports
import math
import numpy as np
import matplotlib.pyplot as plt

#%% SECTION 1 - CALCULATION OF RESTITUTION ARRAYS
# Constants
h = 0.35  # height in meters


# Data arrays
angles = [10, 10, 15, 15, 20, 20, 25, 25]
materials = ["Glass", "Steel", "Glass", "Steel", "Glass", "Steel", "Glass", "Steel"]
distances = [305.3/1000, 226.4/1000, 449.6/1000, 331.9/1000, 
            551.2/1000, 374.8/1000, 527.1/1000, 386.6/1000]  # Converting mm to m


def calculate_e(d, theta):
    """
    Rearranged formula to solve for e:
    d = 2h*sin(2θ)(e*cos²(θ) - sin²(θ))(1+e)
    """
    theta_rad = math.radians(theta)
    sin_2theta = math.sin(2 * theta_rad)
    cos_theta_sq = math.cos(theta_rad) ** 2
    sin_theta_sq = math.sin(theta_rad) ** 2
    
    
    # Coefficients for quadratic equation: ae² + be + c = 0
    a = 2 * h * sin_2theta * cos_theta_sq
    b = 2 * h * sin_2theta * (cos_theta_sq - sin_theta_sq)
    c = -2 * h * sin_2theta * sin_theta_sq - d
    
    # Quadratic formula: e = (-b ± √(b² - 4ac))/(2a)
    # We want the positive root as e should be positive
    discriminant = math.sqrt(b**2 - 4*a*c)
    e = (-b + discriminant)/(2*a)
    
    return e

# Calculate and store results
results = []
for i in range(len(angles)):
    e = calculate_e(distances[i], angles[i])
    results.append({
        "angle": angles[i],
        "type": materials[i],
        "distance": distances[i],
        "coefficient_of_restitution": e
    })

# Print results for Glass
print("Glass Coefficients of Restitution:")
print("Angle (degrees) | Coefficient")
print("-" * 30)
for r in results:
    if r["type"] == "Glass":
        print(f"{r['angle']:13} | {r['coefficient_of_restitution']:.4f}")

# Print results for Steel
print("\nSteel Coefficients of Restitution:")
print("Angle (degrees) | Coefficient")
print("-" * 30)
for r in results:
    if r["type"] == "Steel":
        print(f"{r['angle']:13} | {r['coefficient_of_restitution']:.4f}")
#%% SECTION 2 - PLOTTING OF RESULTS


# Data from our calculations
angles = np.array([10, 15, 20, 25])
glass_e = np.array([0.827, 0.842, 0.859, 0.831])
steel_e = np.array([0.651, 0.667, 0.673, 0.659])

# Calculate averages
glass_avg = np.mean(glass_e)
steel_avg = np.mean(steel_e)

# Create the figure and axis
plt.figure(figsize=(10, 6))

# Plot scatter points with cross markers
plt.scatter(angles, glass_e, color='blue', label='Glass', marker='x', s=100)
plt.scatter(angles, steel_e, color='red', label='Steel', marker='x', s=100)

# Plot average lines
plt.axhline(y=glass_avg, color='blue', linestyle='--', alpha=0.5)
plt.axhline(y=steel_avg, color='red', linestyle='--', alpha=0.5)

# Add text for average values 
plt.text(22, glass_avg + 0.01, f'Glass avg: {glass_avg:.3f}', 
         color='blue', verticalalignment='bottom')
plt.text(22, steel_avg + 0.01, f'Steel avg: {steel_avg:.3f}', 
         color='red', verticalalignment='bottom')

'''
# FOR QUADRATIC FIT
glass_z = np.polyfit(angles, glass_e, 2)
steel_z = np.polyfit(angles, steel_e, 2)
x_trend = np.linspace(angles.min(), angles.max(), 100)
glass_trend = np.poly1d(glass_z)
steel_trend = np.poly1d(steel_z)

plt.plot(x_trend, glass_trend(x_trend), '-', color='blue', alpha=0.5)
plt.plot(x_trend, steel_trend(x_trend), '-', color='red', alpha=0.5)
'''

# Customize the plot
plt.xlabel('Deflector Angle (˚)', fontsize=14)
plt.ylabel('Coefficient of Restitution (e)', fontsize=14)
plt.title('Coefficient of Restitution vs Deflector Angle', fontsize=16, pad=20)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Set axis limits for better visualization
plt.ylim(0.6, 0.9)
plt.xlim(8, 27)

# Prevent cutoff and show plot
plt.tight_layout()
plt.show()