import csv
from itertools import product

def generate_child_skus(parent_sku):
    # Define the variations
    variations = {
        'color_temp': ['3500K', '4500K', '6500K', '2700-6500K'],
        'lumens_per_watt': ['130', '140', '150'],
        'color': ['Black', 'White']
    }

    # Generate all combinations
    combinations = product(variations['color_temp'], variations['lumens_per_watt'], variations['color'])

    # Generate child SKUs
    child_skus = []
    for combo in combinations:
        color_temp, lumens, color = combo
        
        # Skip combinations that don't exist in the given list
        if color_temp == '2700-6500K' and lumens != '150':
            continue
        if color_temp == '3500K' and lumens == '150':
            continue
        if color_temp == '4500K' and lumens == '140':
            continue
        
        child_sku = f"{parent_sku}-{color_temp.replace('-', '')}-{lumens}-{color}"
        description = f"{color_temp} Diffused Glow 12W-1 Feet {color}-{lumens} Lum/Watt"
        child_skus.append((child_sku, description))

    return child_skus

def write_to_csv(skus, filename='child_skus.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Child SKU', 'Description'])
        writer.writerows(skus)

if __name__ == "__main__":
    parent_sku = "MS3005-DF-300MM"
    child_skus = generate_child_skus(parent_sku)
    
    # Print the results
    for sku, description in child_skus:
        print(f"SKU: {sku}")
        print(f"Description: {description}")
        print()

    # Write to CSV
    write_to_csv(child_skus)
    print(f"Child SKUs have been written to child_skus.csv")