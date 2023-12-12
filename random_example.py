import numpy as np
import random

# Generating random numbers that add up to a certain number
def generate_random_floats_with_sum(desired_sum, n):
    # Generate n-1 random numbers between 0 and 1
    random_numbers = np.random.rand(n - 1)
    
    # Calculate the sum of the generated numbers
    sum_of_random_numbers = np.sum(random_numbers)
    
    # Normalize the numbers so their sum equals 1
    normalized_numbers = random_numbers / sum_of_random_numbers
    
    # Scale the numbers so their sum equals the desired sum
    scaled_numbers = normalized_numbers * desired_sum
    
    # Add the last element to the array to meet the desired sum
    result = np.append(scaled_numbers, desired_sum - np.sum(scaled_numbers))
    
    return result

# Example
desired_sum = 266666.67
n = 155

resources_planned_project1 = generate_random_floats_with_sum(desired_sum, n)
print(resources_planned_project1)
print("Sum:", np.sum(resources_planned_project1))

# Convert the array to a DataFrame column
column_date = pd.DataFrame({'cost': resources_planned_project1})

# Save the column to a CSV file
column_date.to_csv('output.csv', index=False)