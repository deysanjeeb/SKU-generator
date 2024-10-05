import pandas as pd

# Function to generate child SKUs appending only the unique parts of the Name column
def generate_child_skus_unique(data):
    child_skus = []
    parent_name = None
    parent_sku = None

    for index, row in data.iterrows():
        if row['Type'] == 'variable':
            # Store the parent SKU and Name for the upcoming variations
            parent_sku = row['SKU']
            parent_name = row['Name']
        elif row['Type'] == 'variation' and parent_sku and parent_name:
            # Extract unique part by removing the common part with the parent Name
            variation_name = row['Name']
            unique_part = variation_name.replace(parent_name, "").strip().replace(" ", "-").replace(",", "").replace("/", "-")
            unique_part = unique_part.replace("--", "-")
            child_sku = f"{parent_sku}-{unique_part}" if unique_part else parent_sku  # If no unique part, just use parent SKU
            child_skus.append({
                'Parent SKU': parent_sku,
                'Variation Name': row['Name'],
                'Generated Child SKU': child_sku
            })

    return pd.DataFrame(child_skus)

# Load your CSV file
filename = 'Ultra thin magnetic product'
file_path = f'{filename}.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Generate the child SKUs with unique parts
child_sku_unique_df = generate_child_skus_unique(data)

# Save the new unique child SKUs to a CSV file
output_file_path = f'{filename}_child_skus.csv'  # Path to save the output
child_sku_unique_df.to_csv(output_file_path, index=False)

print(f"Generated child SKUs saved to {output_file_path}")
